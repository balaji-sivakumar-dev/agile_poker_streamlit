import time
import json
import sqlite3
import streamlit as st
import pandas as pd

from util import init_db, display_session_data,  create_session_data


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
            st.query_params["sessionid"] = session_id
            st.query_params["type"] = "Admin"
            st.query_params["user"] = user_name
            st.rerun()
            
           

#login_create_session()
