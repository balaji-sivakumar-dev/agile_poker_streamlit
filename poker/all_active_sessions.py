import time
import json
import sqlite3
import streamlit as st
import pandas as pd

from util import delete_all_sessions, display_all_session_data

def all_active_sessions():
    st.title("Active Sessions")
    display_all_session_data()
    
    # delete_all_sessions()
    if st.button("Delete All Sessions"):
        delete_all_sessions()
        st.success("All sessions deleted successfully!")
        st.rerun()
    

# active_sessions()