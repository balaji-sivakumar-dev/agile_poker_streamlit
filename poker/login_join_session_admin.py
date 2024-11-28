import time
import json
import sqlite3
import streamlit as st
import pandas as pd

from util import add_session, update_session, get_session, init_db, display_session_data, join_session, create_session_data


# Login screen
def login_join_admin():
    # reset st.query_params
    st.query_params = {}
    st.title("Login as Admin")
      # Initialize session state if it doesn't exist
    if 'session_id' not in st.session_state:
        st.session_state.session_id = ""
   
    user_name = st.text_input("Enter your name:")
    session_id = st.text_input("Enter Session ID:", value=str(st.session_state.session_id) if str(st.session_state.session_id) else "")
    
    # if current_session_id has a value pre populate in text box 
    

    if st.button("Join Session"):
        if not user_name.strip():
            st.error("User name cannot be empty.")
        elif not session_id.isdigit():
            st.error("Session ID must be a number.")
        else:
            session_id = int(session_id)
            success = join_session(session_id, user_name, "Admin")
            if success:
                session_data = get_session(session_id)
                st.success(f"Session '{session_data['name']}' joined successfully!")
                display_session_data(session_id)
               #  st.query_params["sessionid"] = session_id
               # st.query_params["type"] = "Admin"
               # st.query_params["user"] = user_name
               # st.rerun()
