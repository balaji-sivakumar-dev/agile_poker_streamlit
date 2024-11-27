import time
import json

import streamlit as st
import pandas as pd

from header import header
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
        current_session_data = session_state[current_session_id_int]
        print('current_session_data ', current_session_data)
        current_participants = current_session_data["participants"]
        print('current_participants ', current_participants)
        # pretty print the values of global_state
        print (json.dumps(current_participants, indent=2, default=str))
        # st.success(f"Participants in the session are {current_participants}")
        
        # Convert JSON to a list of dictionaries for tabular representation
        table_data = [{'User': user, 'Points': points} for user, points in current_participants.items()]

        # dislay data only if table_data is not empty
        if table_data:
            # Create a DataFrame from the table data
            df = pd.DataFrame(table_data)
            # Display the table in Streamlit
            st.write("User Points Table")
            st.table(df)  # Use st.dataframe(df) if you want interactivity

def set_session_state(session_id, user_type, user_name):
    st.session_state["current_session"] = session_id
    st.session_state["user_type"] = user_type
    st.session_state["user"] = user_name
            
    st.query_params["sessionid"] = session_id
    st.query_params["user_type"] = user_type
    st.query_params["user"] = user_name   

def pointing_poker(session_id, user_name):
    # header()
    st.title("Pointing Poker")
    print('pointing_poker session_id ', session_id, ' user_name ', user_name)
    values = ["NA", 0.25, 0.5, 1, 2, 3, 5, 8 ]
    selected_point = st.radio("Select a point value:", values)
    print('selected_point ', selected_point)

    if st.button("Submit Points"):
        session_data = global_state["sessions"].get(session_id)
        if session_data and user_name in session_data["participants"]:
            session_data["participants"][user_name] = selected_point
            st.success(f"Point '{selected_point}' submitted!")
        else:
            st.error("Invalid session or user.")

def login_screen():
    # header()
    st.title("Login")

    user_type = st.radio("Select your role:", ["Create a Session", "Join as Participant",  "Join as Admin"])
    user_name = st.text_input("Enter your name:")
    

    # print('before submitting global_state ', global_state)
    # print('before submitting  user_type ', user_type)
    # session_id = 0
    # session_id_int = 0

    if user_type == "Create a Session":
        if st.button("Start New Session"):
            session_id_int = int(time.time())  # Timestamp-based session ID          
            add_admin(session_id_int, user_name)
            
            set_session_state(session_id_int, "Admin", user_name)
            # st.rerun()
            print_session_data(session_id_int)        
            if st.button("Refresh"):
                print_session_data(session_id_int)
    elif user_type == "Join as Admin":
        
        session_id = st.text_input("Enter Session ID to join:")
        if st.button("Join Session"):
            session_id_int = int(session_id)
            
            add_admin(session_id_int, user_name)
            set_session_state(session_id_int, "Admin", user_name)
            print('refreshing session_id_int ', session_id_int)
            print_session_data(session_id_int)        
            if st.button("Refresh"):
                print_session_data(session_id_int)
        
    elif user_type == "Join as Participant":
        session_id = st.text_input("Enter Session ID to join:")
        if st.button("Join Session"):
            session_id_int = int(session_id)
            add_participant(session_id_int, user_name)  
            set_session_state(session_id_int, "Participant", user_name)
            print_session_data(session_id_int)        
            pointing_poker(session_id_int, user_name) 

        
    # print values of global_state
    # print('after submitting global_state ', global_state)
    # print_session_data(session_id_int)        


    


