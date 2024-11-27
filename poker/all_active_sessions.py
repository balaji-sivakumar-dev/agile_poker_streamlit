import time
import json
import sqlite3
import streamlit as st
import pandas as pd

from util import display_all_session_data

def all_active_sessions():
    st.title("Active Sessions")
    display_all_session_data()

# active_sessions()