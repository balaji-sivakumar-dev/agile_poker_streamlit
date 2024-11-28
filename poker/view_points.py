# Description: This file contains the code to view the selected points for a session and all active sessions.
import streamlit as st
import pandas as pd

from util import delete_session, display_session_data, display_all_session_data, delete_all_sessions

def view_points():
    st.title("View Selected Points")
    # Initialize session state if it doesn't exist
    if 'session_id' not in st.session_state:
        st.session_state.session_id = ""
        
    session_id = st.text_input("Enter Session ID:" , value=str(st.session_state.session_id) if str(st.session_state.session_id) else "")
    
    if not session_id:
        st.error("Session ID cannot be empty.")
    else:
        session_id_int = int(session_id)
        display_session_data(session_id_int)

    # Delete Current Session Data 
    if st.button("Delete Current Session Data"):
        delete_session(session_id_int)
        st.success("Session data deleted successfully!")
        st.rerun()

def all_active_sessions():
    st.title("Active Sessions")
    display_all_session_data()
    
    # delete_all_sessions()
    if st.button("Delete All Sessions"):
        delete_all_sessions()
        st.success("All sessions deleted successfully!")
        st.rerun()