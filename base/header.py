import streamlit as st

def header():
    st.markdown(
        """
        <style>
            .header {
                font-size: 20px;
                font-weight: bold;
                margin-bottom: 20px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<div class="header">Pointing Poker</div>', unsafe_allow_html=True)
    
    st.sidebar.markdown("### Home")
    st.sidebar.markdown("[Active Sessions](#active-sessions)")
    st.sidebar.markdown("[Create Session](#create-session)")
    st.sidebar.markdown("[Join Session](#join-session)")
