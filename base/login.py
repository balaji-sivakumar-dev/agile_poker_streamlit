import streamlit as st
import time
import json
import pandas as pd

from header import header

# Global state for sessions and users

from state import global_state
# global_state = {"sessions": {}}

# create a function to check if a user exists in the session as an admin
def add_admin(session_id, user_name):
    print('add_admin session_id ', session_id, ' user_name ', user_name)
    if session_id == 0:
        return
    if session_id in global_state["sessions"]:
        admins = global_state["sessions"][session_id]["admins"]
        if user_name in admins:
            return
        else:
            admins.append(user_name)
            global_state["sessions"][session_id]["admins"] = admins
        st.success(f" {user_name} joined Session as Admin! Your Session ID is `{session_id}`")
    else:
        global_state["sessions"][session_id] = {"admins": [user_name], "participants": {}}
        print('global_state ', global_state)
        st.success(f" {user_name} created Session as Admin! Your Session ID is `{session_id}`")
            
# create a function to check if a user exists in the session as a participant
def add_participant(session_id, user_name):
    print('add_participant session_id ', session_id, ' user_name ', user_name)
    if session_id == 0:
        return
    if session_id in global_state["sessions"]:
        participants = global_state["sessions"][session_id]["participants"]
        if user_name in participants:
            return
        else:
            participants[user_name] = None
            global_state["sessions"][session_id]["participants"] = participants
        st.success(f" {user_name} joined Session as Participant! Your Session ID is `{session_id}`")
    else:
        st.error("Invalid Session ID")
            
def join_session():
    session_id = st.text_input("Enter Session ID to join:")
    if st.button("Join Session"):
        session_id_int = int(session_id)
        return session_id_int

def refresh(current_session_id_int):
    print('refresh current_session_id_int ', current_session_id_int)
    if st.button("Refresh"):
        print_session_data(current_session_id_int)

def print_session_data(current_session_id_int):
    print('print_session_data current_session_id_int ', current_session_id_int)
    # print the list of participants in the current session using st.write
    session_state = global_state["sessions"]
    
    # if session_state has data then print the participants   
    if current_session_id_int == 0:
        return
    
    if current_session_id_int in session_state:
        
        current_participants = global_state["sessions"][current_session_id_int]["participants"]
        print('participants ', current_participants)
        # pretty print the values of global_state
        print (json.dumps(session_state, indent=2, default=str))
        # st.success(f"Participants in the session are {current_participants}")
        
        # Convert JSON to a list of dictionaries for tabular representation
        table_data = [{'User': user, 'Points': points} for user, points in current_participants.items()]

        # Create a DataFrame from the table data
        df = pd.DataFrame(table_data)

        # Display the table in Streamlit
        st.write("User Points Table")
        st.table(df)  # Use st.dataframe(df) if you want interactivity

def login_screen():
    # header()
    st.title("Login")

    user_type = st.radio("Select your role:", ["Create a Session", "Join as Participant",  "Join as Admin"])
    user_name = st.text_input("Enter your name:")
    

    # print('before submitting global_state ', global_state)
    # print('before submitting  user_type ', user_type)
    session_id = 0
    session_id_int = 0

    if user_type == "Create a Session":
        if st.button("Start New Session"):
            session_id_int = int(time.time())  # Timestamp-based session ID          
            add_admin(session_id_int, user_name)
            # st.session_state["current_session"] = session_id
            # st.session_state["user_type"] = "Admin"
            # st.query_params["sessionid"] = session_id
            # st.rerun()
            print('refreshing session_id_int ', session_id_int)
            refresh(session_id_int)
    elif user_type == "Join as Admin":
        
        session_id = st.text_input("Enter Session ID to join:")
        if st.button("Join Session"):
            session_id_int = int(session_id)
            
            add_admin(session_id_int, user_name)
            print('refreshing session_id_int ', session_id_int)
            refresh(session_id_int)
        
    elif user_type == "Join as Participant":
        session_id = st.text_input("Enter Session ID to join:")
        if st.button("Join Session"):
            session_id_int = int(session_id)
            add_participant(session_id_int, user_name)      
        
    # print values of global_state
    print('after submitting global_state ', global_state)
    print_session_data(session_id_int)        


    


