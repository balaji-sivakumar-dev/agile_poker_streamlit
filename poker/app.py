import streamlit as st

from login_create_session import login_create_session
from login_join_session_admin import login_join_admin
from login_join_session_user import login_join_user
from active_sessions import active_sessions
from util import init_db, display_session_data,  create_session_data


# Main app
def main():
    init_db()
    
    # Get query parameters from the URL
    query_params = st.query_params
    
    session_id = query_params.get("sessionid", [None])[0]
    user_type = query_params.get("type", [None])[0]
    user_name = query_params.get("user", [None])[0]
    
    page = st.sidebar.selectbox("Select Page", ["Create Session", "Join as Admin", "Join as User", "Active Sessions", "login_pointing_poker"])
    if page == "Login":
        login_create_session()
    elif page == "Active Sessions":
        active_sessions()
    elif page == "Join as Admin":
        login_join_admin()
    elif page == "Join as User":
        login_join_user() 
    elif page == "login_pointing_poker":
        login_join_user() 
    else:
        login_create_session()
        
        
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
