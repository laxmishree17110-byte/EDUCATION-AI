import streamlit as st
from google import genai

st.set_page_config(page_title="EduAgent - AI Scheduler", page_icon="📚")

st.title("📚 EduAgent: AI Study Scheduler")
st.write("Turn your syllabus into a daily study timetable in seconds.")

# Sidebar for API Key
with st.sidebar:
    api_key = st.text_input("Enter Gemini API Key", type="password")

# User Inputs
subject = st.text_input("Subject / Exam Name", "Data Structures")
target_days = st.number_input("Days Left for Exam", min_value=1, value=7)
available_hours = st.slider("Daily Available Study Hours", 1, 10, 4)
topics = st.text_area("List Topics/Chapters", "Arrays, Linked Lists, Trees, Sorting Algorithms")

if st.button("🚀 Generate Schedule"):
    if not api_key:
        st.error("Please enter your Gemini API Key in the sidebar!")
    else:
        with st.spinner("Generating plan..."):
            try:
                client = genai.Client(api_key=api_key)
                prompt = f"""
                You are an expert AI study scheduler.
                Subject: {subject}
                Days left: {target_days}
                Daily hours: {available_hours}
                Topics to cover: {topics}
                
                Create a day-by-day timetable showing which topics to study each day and how to divide the hours.
                """
                response = client.models.generate_content(
                    model="gemini-3.6-flash",
                    contents=prompt
                )
                st.success("Done!")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"Error: {e}")
