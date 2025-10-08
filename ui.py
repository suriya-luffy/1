import streamlit as st
from utils import detect_mood_from_face, save_mood_history

def show_mood_dashboard():
    st.title("Mood Dashboard")
    if "user" not in st.session_state:
        st.warning("Please login first!")
        return

    st.write(f"Welcome {st.session_state['user']} 👋")

    mood_input_method = st.radio("How do you want to input your mood?", ["Face Upload", "Text", "Voice"])

    if mood_input_method == "Face Upload":
        image = st.file_uploader("Upload your photo")
        if image:
            mood = detect_mood_from_face(image)
            st.success(f"Detected mood: {mood}")
            save_mood_history(st.session_state["user"], mood)

    elif mood_input_method == "Text":
        mood_text = st.text_input("Describe your mood")
        if st.button("Submit Text Mood"):
            save_mood_history(st.session_state["user"], mood_text)
            st.success(f"Mood recorded: {mood_text}")

    elif mood_input_method == "Voice":
        st.info("Voice mood input coming soon...")
