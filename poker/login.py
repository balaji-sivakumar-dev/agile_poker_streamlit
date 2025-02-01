import time
import json
import sqlite3
import streamlit as st
import pandas as pd

from util import display_session_data,  create_session_data, generate_session_url, join_session, get_session


# Login screen
def login_create_session():
    st.title("Login")
    user_name = st.text_input("Enter your name:")

    if st.button("Start New Session"):
        if not user_name.strip():
            st.error("User name cannot be empty.")
        else:
            session_id = create_session_data(user_name)
            #st.success(f"Session created successfully! Your Session ID is `{session_id}`.")
            
            # Generate and display the session URL
            session_url = generate_session_url(session_id)
            st.info("Share this URL with participants:")
            
            
            st.markdown(f"[copy & share this link](/?page=Join+as+User&session_id={session_id})")
            #st.code(session_url, language="text")
            
            # Display session data
            display_session_data(session_id)
            
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
    # Get session_id from URL parameters
    params = st.query_params

    #default_session_id = params.get("session_id", [""])[0]
    #default_session_id = params.session_id if params.session_id else ""
    default_session_id = params["session_id"] if "session_id" in params else ""
    #default_user_name = params.user if params.user else ""
    default_user_name = params["user"] if "user" in params else ""
    
    # Initialize session state
    if 'session_id' not in st.session_state:
        st.session_state.session_id = default_session_id
    if 'user_name' not in st.session_state:
        st.session_state.user_name = default_user_name or ""
    
    st.title("Login as User")
    user_name = st.text_input("Enter your name:", 
                             value=str(st.session_state.user_name) if str(st.session_state.user_name) else "")
    session_id = st.text_input("Enter Session ID:",
                              value=default_session_id or str(st.session_state.session_id))
    
    selected_point = st.radio(
        "Select a point value:",
        options=["NA", 1, 2, 3, 5, 8]
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
                st.session_state.session_id = session_id
                st.session_state.user_name = user_name

                #st.query_params["sessionid"] = session_id
                #st.query_params["type"] = "User"
                #st.query_params["user"] = user_name
                #st.rerun()