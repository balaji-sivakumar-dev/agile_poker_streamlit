import streamlit as st

# Title and Text
st.title("Hello, Streamlit!")
st.write("This is my first Streamlit app.")

# Input Widgets
name = st.text_input("Enter your name:")
age = st.slider("Select your age:", 1, 100)

# Output
if st.button("Submit"):
    st.write(f"Hello {name}, you are {age} years old!")
