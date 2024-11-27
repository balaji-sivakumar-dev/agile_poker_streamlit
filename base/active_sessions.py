import streamlit as st

from header import header
from state import global_state

def active_sessions():
    header()
    st.title("Active Sessions")
    st.write("Here are the active sessions:")
    for session_id, details in global_state["sessions"].items():
        st.write(f"Session ID: {session_id}")
        st.markdown(f"[Open Session Details](?sessionid={session_id})")
