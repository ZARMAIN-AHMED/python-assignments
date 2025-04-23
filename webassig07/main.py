import streamlit as st

# --- OOP Class for Each Course Topic ---
class CourseTopic:
    def __init__(self, title, description, video_url):
        self.title = title
        self.description = description
        self.video_url = video_url

    def display(self):
        with st.container():
            st.markdown("### 🎯 " + self.title)
            st.markdown(f"**Description:** {self.description}")
            st.video(self.video_url)
            st.markdown("---")


# --- Main Course Class ---
class AgenticAICourse:
    def __init__(self):
        self.topics = {
            "Beginner": [
                CourseTopic(
                    "What is Agentic AI?",
                    "An introduction to agentic systems and their real-world applications.",
                    "https://www.youtube.com/watch?v=-pqzyvRp3Tc"
                ),
                CourseTopic(
                    "Python Crash Course",
                    "Learn Python programming basics like variables, data types, and loops.",
                    "https://www.youtube.com/watch?v=JJmcL1N2KQs"
                ),
                CourseTopic(
                    "Understanding Python Bytecode",
                    "Explore how Python compiles code to bytecode and what it means.",
                    "https://www.youtube.com/watch?v=mE0oR9NQefw"
                ),
            ],
            "Intermediate": [
                CourseTopic(
                    "Dynamic Typing in Python",
                    "Understand how Python handles dynamic typing and variable assignments.",
                    "https://www.youtube.com/watch?v=ba3Qjv_fbVU"
                ),
                CourseTopic(
                    "Type Hinting in Python",
                    "Use type hints for clearer, more predictable code.",
                    "https://www.youtube.com/watch?v=79zeCq9raY0"
                ),
                CourseTopic(
                    "Disassembling with dis Module",
                    "Use Python’s dis module to visualize bytecode.",
                    "https://www.youtube.com/watch?v=2Z1RJDVM0rc"
                ),
            ],
            "Advanced": [
                CourseTopic(
                    "Build AI Agents from Scratch",
                    "Create intelligent autonomous agents.",
                    "https://www.youtube.com/watch?v=_Udb5NC6vTI"
                ),
                CourseTopic(
                    "LangChain for Agentic AI",
                    "Real-world agentic systems using LangChain.",
                    "https://www.youtube.com/watch?v=YgBYQgehCB8"
                ),
                CourseTopic(
                    "Ethics in Agentic AI",
                    "Explore bias, transparency, and accountability in AI.",
                    "https://www.youtube.com/watch?v=VqFqWIqOB1g"
                ),
            ]
        }

    def get_topics(self, level):
        return self.topics.get(level, [])


# --- Streamlit UI ---
st.set_page_config("Agentic AI Course", layout="wide")

with st.sidebar:
    st.title("🧠 Agentic AI")
    st.markdown("### 📘 Full Learning Path")
    selected_level = st.radio("Select your level", ["Beginner", "Intermediate", "Advanced"])
    st.markdown("💡 Tip: Click **Run** to view videos")

st.markdown(
    f"""
    <div style='text-align: center; padding: 10px 0'>
        <h1 style='margin-bottom: 0;'>🚀 Agentic AI Full Course</h1>
        <p style='font-size: 18px;'>Your step-by-step learning journey to mastering Agentic AI</p>
    </div>
    """,
    unsafe_allow_html=True
)

course = AgenticAICourse()

if selected_level:
    st.markdown(f"## 📚 {selected_level} Topics")
    for topic in course.get_topics(selected_level):
        topic.display()
