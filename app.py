# app.py
import streamlit as st
from openai_api import get_interview_response
from utils import format_question

st.set_page_config(page_title="AI Interview Prep Assistant", layout="centered")

st.title("🧠 AI Interview Preparation Assistant")
st.write("Prepare for your technical interviews with AI-generated questions and answers.")

# Input for topic
topic = st.text_input("Enter the topic (e.g., Data Structures, Python, SQL):")

# Select difficulty
difficulty = st.selectbox("Select difficulty level:", ["Easy", "Medium", "Hard"])

# Trigger generation
if st.button("Generate Question & Answer"):
    if topic:
        prompt = format_question(topic, difficulty)
        with st.spinner("Generating your question & answer..."):
            result = get_interview_response(prompt)
        st.success("Here's your generated Interview Q&A:")
        st.write(result)
    else:
        st.warning("Please enter a topic to proceed.")
