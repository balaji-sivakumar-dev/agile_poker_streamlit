import streamlit as st

from active_sessions import active_sessions
from pointing_poker import pointing_poker
from login import login_screen
from session import session_page
from state import global_state

# Main app
def main():
    # Get query parameters from the URL
    query_params = st.query_params
    # initialize with a sample alue 
    # global_state["sessions"] = {1: {"name": "Session 1", "participants": ["Alice", "Bob", "Charlie"]}}

    # Print the query parameters (for debugging)
    # st.write(query_params)
    
    session_id = query_params.get("sessionid", [None])[0]
    user_name = query_params.get("user", [None])[0]
    
    login_screen()
    # page = st.sidebar.selectbox("Select Page", ["Login", "Active Sessions"])
    # if page == "Login":
        #login_screen()
    # elif page == "Active Sessions":
       # active_sessions()
        
        
    #
       # if session_id:
       # session_id = int(session_id)
       # if user_name:
       #     pointing_poker(session_id, user_name)
       # else:
       #     session_page(session_id)
    # else:

if __name__ == "__main__":
    main()
