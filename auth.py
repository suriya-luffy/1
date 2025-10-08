import streamlit as st
import bcrypt
from db_models import add_user, get_user

def signup_user():
    st.title("Signup")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Signup"):
        hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        add_user(username, hashed)
        st.success("Account created successfully!")

def login_user():
    st.title("Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        user = get_user(username)
        if user and bcrypt.checkpw(password.encode(), user.password.encode()):
            st.session_state["user"] = username
            st.success("Login successful!")
        else:
            st.error("Invalid credentials")
