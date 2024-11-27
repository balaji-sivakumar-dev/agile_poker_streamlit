import streamlit as st

from header import header
from state import global_state

def session_page(session_id):
    header()
    st.title(f"Session {session_id}")

    session_data = global_state["sessions"].get(session_id)
    if not session_data:
        st.error("Invalid Session ID")
        return

    st.subheader("Users in Session:")
    for user, points in session_data["participants"].items():
        st.write(f"{user}: {points if points else 'No point submitted'}")

    if st.session_state.get("user_type") == "Admin":
        if st.button("Reset Points"):
            for user in session_data["participants"]:
                session_data["participants"][user] = None
            session_data["points_reset"] = True
            st.success("Points have been reset.")
