import streamlit as st

from login import login_create_session, login_join_admin, login_join_user
from view_points import view_points, all_active_sessions
from util import init_db


# Main app
def main():
    init_db()
    
    
    # Get the page from URL parameters
    params = st.query_params
    print("params " , params)
    #default_page = params.get("page", ["Create Session"])[0]
    # default_page = params.page if params.page else "Create Session"
    default_page = params["page"] if "page" in params else "Create Session"
    
    page = st.sidebar.selectbox(
        "Select Page",
        ["Create Session", "Join as User", "View Selected Points", "Join as Admin", "Active Sessions"],
        index=["Create Session", "Join as User", "View Selected Points", "Join as Admin", "Active Sessions"].index(default_page)
    )
    
    if page == "Create Session":
        login_create_session()
    elif page == "Join as Admin":
        login_join_admin()
    elif page == "Join as User":
        login_join_user()
    elif page == "View Selected Points":
        view_points()
    elif page == "Active Sessions":
        all_active_sessions()
        
if __name__ == "__main__":
    main()
