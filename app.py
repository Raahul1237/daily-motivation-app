import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the Gemini Pro model
model = genai.GenerativeModel("gemini-2.5-flash")

# Streamlit UI setup
st.set_page_config(page_title="Daily Motivation Generator", page_icon="💪", layout="centered")
st.title("💡 Daily Motivation Generator")
st.markdown("Feeling stuck or need a boost? Select your mood or situation and get an encouraging quote!")

# Mood dropdown
moods = [
    "Feeling anxious", "Need focus", "Lack of motivation", "Feeling sad", "Self-doubt",
    "Facing a challenge", "Burnout", "Low energy", "Starting the day", "Ending the day"
]
selected_mood = st.selectbox("Choose your current situation or mood:", moods)

# Generate motivation using Gemini
def generate_motivation(mood):
    prompt = f"Write a short and powerful motivational quote for someone who is {mood.lower()}."
    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error: {e}"

# Button and display
if st.button("Generate Motivation ✨"):
    with st.spinner("Crafting your motivation..."):
        quote = generate_motivation(selected_mood)
        st.success("Here's your quote:")
        st.markdown(f"> 🌟 *{quote}*")
