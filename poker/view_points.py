import time
import json
import sqlite3
import streamlit as st
import pandas as pd

from util import display_session_data

def view_points():
    st.title("View Selected Points")
    session_id = st.text_input("Enter Session ID:")
    
    if not session_id:
        st.error("Session ID cannot be empty.")
    else:
        session_id_int = int(session_id)
        display_session_data(session_id_int)

# active_sessions()