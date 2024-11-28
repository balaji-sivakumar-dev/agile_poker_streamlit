import streamlit as st

from login_create_session import login_create_session
from login_join_session_admin import login_join_admin
from login_join_session_user import login_join_user
from view_points import view_points
from util import init_db, display_session_data,  create_session_data
from all_active_sessions import all_active_sessions


# Main app
def main():
    init_db()
    
    
    page = st.sidebar.selectbox("Select Page", ["Create Session", "Join as User", "View Selected Points" , "Join as Admin",  "Active Sessions"])
    if page == "Login":
        login_create_session()
    
    elif page == "Join as Admin":
        login_join_admin()
    elif page == "Join as User":
        login_join_user()
    elif page =="View Selected Points":
        view_points()
    elif page == "Active Sessions":
        all_active_sessions()
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
