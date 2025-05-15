# # utils.py
# import streamlit as st

# def require_login():
#     if "user" not in st.session_state or st.session_state.user is None:
#         st.warning("🔒 Please log in to continue.")
#         st.stop()
import streamlit as st

def require_login():
    if not st.session_state.user:
        st.error("Please log in to continue.")
        st.stop()
