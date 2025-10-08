import random
import streamlit as st
import sqlite3

MOODS = ["Happy", "Sad", "Excited", "Calm", "Angry", "Surprised"]

def detect_mood_from_face(image):
    try:
        from deepface import DeepFace
        import tempfile, os
        with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
            tmp.write(image.read())
            tmp_path = tmp.name
        result = DeepFace.analyze(img_path=tmp_path, actions=["emotion"], enforce_detection=False)
        os.remove(tmp_path)
        return result[0]["dominant_emotion"].capitalize()
    except Exception as e:
        st.warning(f"Facial recognition not available or failed: {e}")
        return random.choice(MOODS)

def save_mood_history(username, mood):
    conn = sqlite3.connect("mood_app.db")
    c = conn.cursor()
    c.execute("INSERT INTO mood_history (username, mood) VALUES (?, ?)", (username, mood))
    conn.commit()
    conn.close()
