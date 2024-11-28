import time
import json
import sqlite3
import streamlit as st
import pandas as pd

from util import display_session_data,  create_session_data, join_session, get_session


# Login screen
def login_create_session():
    # reset st.query_params
    st.query_params = {}
    st.title("Login")
    user_name = st.text_input("Enter your name:")

    if st.button("Start New Session"):
        if not user_name.strip():
            st.error("User name cannot be empty.")
        else:
            session_id = create_session_data(user_name)
           #  display_session_data(session_id)
            # st.query_params["sessionid"] = session_id
            # st.query_params["type"] = "Admin"
            # st.query_params["user"] = user_name
            # st.rerun()
            
           
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

# Login screen
def login_join_user():
    # Initialize session state if it doesn't exist
    if 'session_id' not in st.session_state:
        st.session_state.session_id = ""
    
    # reset st.query_params
    st.query_params = {}
    st.title("Login as User")
    user_name = st.text_input("Enter your name:", value=str(st.session_state.user_name) if str(st.session_state.user_name) else "")
    session_id = st.text_input(
        "Enter Session ID:",
        value=str(st.session_state.session_id) if str(st.session_state.session_id) else ""
    )
    
    selected_point = st.radio(
        "Select a point value:",
        options=[1, 2, 3, 5, 8, "NA"]
    )
    
    if st.button("Vote"):
        if not user_name.strip():
            st.error("User name cannot be empty.")
        elif not session_id.isdigit():
            st.error("Session ID must be a number.")
        else:
            session_id = int(session_id)
            success = join_session(session_id, user_name, "User", selected_point)
            if success:
                st.success(f"User '{user_name}' Voted '{selected_point}' successfully!")
                #st.query_params["sessionid"] = session_id
                #st.query_params["type"] = "User"
                #st.query_params["user"] = user_name
                #st.rerun()