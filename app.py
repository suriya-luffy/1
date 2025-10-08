import streamlit as st
from auth import login_user, signup_user
from ui import show_mood_dashboard
from db_models import init_db

st.set_page_config(page_title="AI Music Mood Player", layout="wide")

init_db()

menu = st.sidebar.selectbox("Menu", ["Login", "Signup", "Dashboard"])

if menu == "Signup":
    signup_user()
elif menu == "Login":
    login_user()
elif menu == "Dashboard":
    show_mood_dashboard()
