from header import header
import streamlit as st
from state import global_state

def pointing_poker(session_id, user_name):
    # header()
    st.title("Pointing Poker")
    print('pointing_poker session_id ', session_id, ' user_name ', user_name)
    values = [0.25, 0.5, 1, 2, 3, 5, 8, "NA"]
    selected_point = st.radio("Select a point value:", values)
    print('selected_point ', selected_point)

    if st.button("Submit Points"):
        session_data = global_state["sessions"].get(session_id)
        if session_data and user_name in session_data["participants"]:
            session_data["participants"][user_name] = selected_point
            st.success(f"Point '{selected_point}' submitted!")
        else:
            st.error("Invalid session or user.")
