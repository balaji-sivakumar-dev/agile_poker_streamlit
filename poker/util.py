import json
import sqlite3
import time
import streamlit as st
import pandas as pd

DB_FILE = "sessions.db"

# ### Database Functions ###

# Initialize the SQLite database
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY,
            admins TEXT,
            participants TEXT
        )
    """)
    conn.commit()
    conn.close()


# Database helper functions
def add_session(session_id, admins, participants):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO sessions (id, admins, participants)
        VALUES (?, ?, ?)
    """, (session_id, json.dumps(admins), json.dumps(participants)))
    conn.commit()
    conn.close()


def update_session(session_id, admins, participants):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE sessions
        SET admins = ?, participants = ?
        WHERE id = ?
    """, (json.dumps(admins), json.dumps(participants), session_id))
    conn.commit()
    conn.close()


def get_session(session_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("SELECT admins, participants FROM sessions WHERE id = ?", (session_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        return {"admins": json.loads(row[0]), "participants": json.loads(row[1])}
    return None

def display_all_session_data():
    conn = sqlite3.connect(DB_FILE)
    df = pd.read_sql_query("SELECT * FROM sessions", conn)
    # Remove the index column
    df = df.reset_index(drop=True)
    conn.close()
    st.write("All Sessions:")
    # Convert DataFrame to a dictionary without the index column
    df_dict = df.to_dict('records')

    # Display the DataFrame without the index column
    st.table(df_dict)

def delete_all_sessions():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sessions")
    conn.commit()
    conn.close()
    
def delete_session(session_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM sessions WHERE id = ?", (session_id,))
    conn.commit()
    conn.close()

# ## Managing Session Data ##

# Core application logic
def create_session_data(user_name):
    session_id = int(time.time())
    add_session(session_id, [user_name], {})
    st.session_state["current_session_id"] = session_id
    st.session_state["user_name"] = user_name
    st.session_state["user_type"] = "Admin"
    st.success(f"Session created successfully! Your Session ID is `{session_id}`.")
    return session_id

def display_session_data(session_id):
    session_data = get_session(session_id)
    if not session_data:
        st.error("Session not found.")
        return

    participants = session_data["participants"]
    if participants:
        table_data = [{"User": user, "Points": points} for user, points in participants.items()]
        df = pd.DataFrame(table_data)
        # Remove the index column
        df = df.reset_index(drop=True)

        st.write("Participants and Points:")
        
        # Convert DataFrame to a dictionary without the index column
        df_dict = df.to_dict('records')

        # Display the DataFrame without the index column
        st.table(df_dict)
    else:
        st.write("No participants yet.")
        
    
def join_session(session_id, user_name, user_type, selected_point=None):
    session_data = get_session(session_id)
    if not session_data:
        st.error("Invalid Session ID.")
        return False

    admins = session_data["admins"]
    participants = session_data["participants"]

    if user_type == "Admin":
        if user_name not in admins:
            admins.append(user_name)
    elif user_type == "User":
        if user_name not in participants:
            participants[user_name] = selected_point

    update_session(session_id, admins, participants)

    st.session_state["current_session_id"] = session_id
    st.session_state["user_name"] = user_name
    st.session_state["user_type"] = user_type

    # st.success(f"Joined session `{session_id}` as {user_type}.")
    return True

