import streamlit as st
import pandas as pd
import re
import zipfile
import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod
from typing import List
from PIL import Image


class CyberSecurityTool(ABC):
    """Abstract Base Class for all Cybersecurity tools."""
    @abstractmethod
    def run(self):
        pass


class App:
    """Represents a Mobile App with its permissions."""
    def __init__(self, name: str, permissions: List[str]):
        self.name = name
        self.permissions = permissions


class AppAnalyzer(CyberSecurityTool):
    """Analyzes app permissions and calculates risk scores."""
    risky_permissions = {
        "READ_SMS", "RECORD_AUDIO", "ACCESS_FINE_LOCATION",
        "READ_CONTACTS", "READ_CALL_LOG", "SEND_SMS", "CAMERA"
    }

    def __init__(self, apps: List[App]):
        self.apps = apps

    def run(self):
        report = []
        for app in self.apps:
            risky = [perm for perm in app.permissions if perm in self.risky_permissions]
            score = self._calculate_risk_score(risky)
            suggestion = self._get_suggestion(score)
            report.append({
                "name": app.name,
                "risky_permissions": risky,
                "risk_score": score,
                "suggestion": suggestion
            })
        return report

    def _calculate_risk_score(self, risky_permissions):
        """Encapsulated risk score calculation."""
        return min(len(risky_permissions) * 15, 100)

    def _get_suggestion(self, score):
        """Encapsulated suggestion generation."""
        if score >= 70:
            return "⚠️ High Risk! Uninstall or limit permissions."
        elif score >= 40:
            return "⚠️ Medium Risk. Review permissions."
        else:
            return "✅ Low Risk."


class PhishingURLChecker(CyberSecurityTool):
    """Detects phishing URLs based on patterns."""
    def __init__(self, url: str):
        self.url = url

    def run(self):
        suspicious_signs = [
            r"https?://\d{1,3}(\.\d{1,3}){3}",    # IP in URL
            r"@\w+",                              # @ symbol
            r"(login|secure|account|bank).*\.com",# Keyword traps
            r"https?://.*\.(ru|cn|tk|ml|ga)",      # Suspicious TLDs
            r"[A-Za-z0-9]{10,}\.com"              # Random domain
        ]
        return self._check_for_suspicious_patterns(suspicious_signs)

    def _check_for_suspicious_patterns(self, patterns):
        """Encapsulated pattern checking."""
        for pattern in patterns:
            if re.search(pattern, self.url):
                return "⚠️ Suspicious URL! Avoid clicking."
        return "✅ Safe URL."


class MultiFileAnalyzer:
    """Handles the analysis and preview of multiple file formats."""
    def __init__(self, file):
        self.file = file
        self.file_name = file.name.lower()

    def analyze(self):
        try:
            if self.file_name.endswith(".txt"):
                return self._analyze_txt()
            elif self.file_name.endswith(".json"):
                return self._analyze_json()
            elif self.file_name.endswith(".xml"):
                return self._analyze_xml()
            elif self.file_name.endswith((".jpg", ".jpeg", ".png")):
                return self._analyze_image()
            elif self.file_name.endswith(".zip"):
                return self._analyze_zip()
            else:
                return "⚠️ Unsupported file type."
        except Exception as e:
            return f"⚠️ Error processing file: {e}"

    def _analyze_txt(self):
        """Encapsulated text file analysis."""
        return self.file.read().decode("utf-8")

    def _analyze_json(self):
        """Encapsulated JSON file analysis."""
        data = json.load(self.file)
        return json.dumps(data, indent=4)

    def _analyze_xml(self):
        """Encapsulated XML file analysis."""
        tree = ET.parse(self.file)
        root = tree.getroot()
        return ET.tostring(root, encoding="unicode")

    def _analyze_image(self):
        """Encapsulated image file analysis."""
        image = Image.open(self.file)
        return image

    def _analyze_zip(self):
        """Encapsulated ZIP file analysis."""
        with zipfile.ZipFile(self.file, "r") as zip_ref:
            return "\n".join(zip_ref.namelist())


# === Streamlit Setup ===
st.set_page_config(page_title="Cyber Threat Toolkit", page_icon="🛡️", layout="centered")
st.title("🛡️ Cyber Threat Toolkit (Python + Streamlit + OOP)")

st.sidebar.title("🔍 Tool Guide")
st.sidebar.info(
    """
    - 📱 **App Scanner**: Upload a CSV file with App names and permissions.
    - 🌐 **URL Checker**: Enter a suspicious URL for analysis.
    - 📁 **Multi File Viewer**: Upload TXT, JSON, PDF, XML, ZIP, or Images.
    """
)

# === Tabs ===
tab1, tab2, tab3 = st.tabs([
    "📱 App Permission Scanner",
    "🌐 Phishing URL Checker",
    "📁 Multi-File Analyzer"
])

# === Tab 1: App Scanner ===
with tab1:
    st.header("📱 Mobile App Risk Scanner")
    st.markdown("Upload a **CSV file** with `App` and `Permissions` columns (permissions separated by semicolon `;`).")

    with st.expander("📥 Download Sample CSV"):
        sample_df = pd.DataFrame({
            "App": ["ChatApp", "MapTracker"],
            "Permissions": ["CAMERA;RECORD_AUDIO", "ACCESS_FINE_LOCATION;READ_CONTACTS"]
        })
        st.download_button("Download Sample", sample_df.to_csv(index=False), "sample_apps.csv", "text/csv")

    uploaded_file = st.file_uploader("Upload App CSV File", type=["csv"])

    if uploaded_file:
        try:
            df = pd.read_csv(uploaded_file)
            apps = [
                App(name=row["App"], permissions=row["Permissions"].split(';'))
                for _, row in df.iterrows()
            ]
            analyzer = AppAnalyzer(apps)
            results = analyzer.run()

            st.success("✅ Analysis Complete!")

            for app in results:
                with st.expander(f"📱 App: {app['name']}"):
                    st.write(f"**Risky Permissions:** {', '.join(app['risky_permissions']) or 'None'}")
                    st.progress(app['risk_score'] / 100)
                    st.markdown(f"🔐 **Risk Score:** `{app['risk_score']}/100`")
                    st.markdown(f"🧠 **Suggestion:** {app['suggestion']}")

        except Exception as e:
            st.error(f"❌ Error processing file: {e}")

# === Tab 2: URL Checker ===
with tab2:
    st.header("🌐 Phishing URL Detector")
    url = st.text_input("🔗 Enter a suspicious URL", placeholder="https://secure-login123.tk")

    if st.button("Analyze URL"):
        if url:
            checker = PhishingURLChecker(url)
            result = checker.run()
            if "Suspicious" in result:
                st.error(result)
            else:
                st.success(result)
        else:
            st.warning("Please enter a valid URL.")

# === Tab 3: Multi File Analyzer ===
with tab3:
    st.header("📁 File Content Viewer & Analyzer")
    other_file = st.file_uploader("Upload Any File (.txt, .json, .pdf, .xml, .jpg, .png, .zip)", type=[
        "txt", "json", "pdf", "xml", "jpg", "jpeg", "png", "zip"
    ])

    if other_file:
        file_analyzer = MultiFileAnalyzer(other_file)
        result = file_analyzer.analyze()

        if isinstance(result, str):
            st.code(result)
        else:
            st.image(result, caption="Preview", use_container_width=True)

# === Footer ===
st.markdown("---")
st.caption("Made with ❤️ by Zarmain Ahmed")
