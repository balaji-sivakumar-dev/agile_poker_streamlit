import time
import json
import sqlite3
import streamlit as st
import pandas as pd

from util import add_session, update_session, get_session, init_db




# Core application logic
def create_session(user_name):
    session_id = int(time.time())
    add_session(session_id, [user_name], {})
    st.session_state["current_session_id"] = session_id
    st.session_state["user_name"] = user_name
    st.session_state["user_type"] = "Admin"
    st.success(f"Session created successfully! Your Session ID is `{session_id}`.")
    return session_id


def join_session(session_id, user_name, user_type):
    session_data = get_session(session_id)
    if not session_data:
        st.error("Invalid Session ID.")
        return False

    admins = session_data["admins"]
    participants = session_data["participants"]

    if user_type == "Admin":
        if user_name not in admins:
            admins.append(user_name)
    elif user_type == "Participant":
        if user_name not in participants:
            participants[user_name] = None

    update_session(session_id, admins, participants)

    st.session_state["current_session_id"] = session_id
    st.session_state["user_name"] = user_name
    st.session_state["user_type"] = user_type

    st.success(f"Joined session `{session_id}` as {user_type}.")
    return True


def display_session_data(session_id):
    session_data = get_session(session_id)
    if not session_data:
        st.error("Session not found.")
        return

    participants = session_data["participants"]
    if participants:
        table_data = [{"User": user, "Points": points} for user, points in participants.items()]
        df = pd.DataFrame(table_data)
        st.write("Participants and Points:")
        st.table(df)
    else:
        st.write("No participants yet.")


def pointing_poker(session_id, user_name):
    st.title("Pointing Poker")
    session_data = get_session(session_id)

    if not session_data:
        st.error("Session not found.")
        return

    participants = session_data["participants"]

    # Retrieve the current user's selected point
    selected_point = participants.get(user_name, "NA")

    # Radio button for selecting a point value
    values = ["NA", 0.25, 0.5, 1, 2, 3, 5, 8]
    selected_point = st.radio(
        "Select a point value:",
        values,
        index=values.index(selected_point) if selected_point in values else 0,
        key=f"point_{session_id}_{user_name}"
    )

    # Submit button to save the selected point
    if st.button("Submit Points", key=f"submit_{session_id}_{user_name}"):
        participants[user_name] = selected_point
        update_session(session_id, session_data["admins"], participants)
        st.success(f"Point '{selected_point}' submitted!")

    # Display the updated participants and points
    st.write("Current Points:")
    display_session_data(session_id)


# Login screen
def login_screen():
    st.title("Login")
    user_name = st.text_input("Enter your name:")
    role = st.radio("Select your role:", ["Create a Session", "Join as Admin", "Join as Participant"])

    if role == "Create a Session":
        if st.button("Start New Session"):
            if not user_name.strip():
                st.error("User name cannot be empty.")
            else:
                session_id = create_session(user_name)
                display_session_data(session_id)
    elif role in ["Join as Admin", "Join as Participant"]:
        session_id = st.text_input("Enter Session ID:")
        if st.button("Join Session"):
            if not user_name.strip():
                st.error("User name cannot be empty.")
            elif not session_id.isdigit():
                st.error("Session ID must be a number.")
            else:
                session_id = int(session_id)
                success = join_session(session_id, user_name, role.split()[-1])
                if success and role == "Join as Participant":
                    pointing_poker(session_id, user_name)
                elif success:
                    display_session_data(session_id)


# Run the app
init_db()
login_screen()
