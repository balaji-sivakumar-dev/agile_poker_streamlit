import streamlit as st
import time

from header import header

# Global state for sessions and users

from state import global_state
global_state = {"sessions": {}}

def login_screen():
    header()
    st.title("Login")

    user_type = st.radio("Select your role:", ["Admin", "Participant"])
    user_name = st.text_input("Enter your name:")

    if user_type == "Admin":
        if st.button("Start New Session"):
            session_id = int(time.time())  # Timestamp-based session ID
            global_state["sessions"][session_id] = {"admin": user_name, "participants": {}, "points_reset": False}
            st.success(f"Session created! Your Session ID is {session_id}")
            st.session_state["current_session"] = session_id
            st.session_state["user_type"] = "Admin"
            st.query_params["sessionid"] = session_id
            st.rerun()

    elif user_type == "Participant":
        session_id = st.text_input("Enter Session ID to join:")
        if st.button("Join Session"):
            if int(session_id) in global_state["sessions"]:
                global_state["sessions"][int(session_id)]["participants"][user_name] = None
                st.session_state["current_session"] = int(session_id)
                st.session_state["user_type"] = "Participant"
                st.session_state["user_name"] = user_name
                st.query_params["sessionid"] = session_id
                st.query_params["user"] = user_name
                st.rerun()
            else:
                st.error("Invalid Session ID")
