import time
import json
import sqlite3
import streamlit as st
import pandas as pd

from util import add_session, update_session, get_session, init_db, display_session_data, join_session, create_session_data

def pointing_poker(session_id, user_name):
    st.title("Pointing Poker")
    session_data = get_session(session_id)

    if not session_data:
        st.error("Session not found.")
        return

    participants = session_data["participants"]

    # Initialize session state if it doesn't exist
    if 'selected_point' not in st.session_state:
        st.session_state.selected_point = None
    
    # Retrieve the current user's selected point
    selected_point = participants.get(user_name, "NA")

    # Radio button to select a point value
    selected_point = st.radio(
        "Select a point value:",
        options=[1, 2, 3, 4, 5],
        index=st.session_state.selected_point if st.session_state.selected_point is not None else 0
    )
    
    # Update session state
    st.session_state.selected_point = selected_point
    st.write(f"Selected point value: {selected_point}")

    # Submit button to save the selected point
    if st.button("Submit Points", key=f"submit_{session_id}_{user_name}"):
        participants[user_name] = selected_point
        update_session(session_id, session_data["admins"], participants)
        st.success(f"Point '{selected_point}' submitted!")


# Login screen
def login_join_user():
    # reset st.query_params
    st.query_params = {}
    st.title("Login as User")
    user_name = st.text_input("Enter your name:")
    session_id = st.text_input("Enter Session ID:")
    
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


