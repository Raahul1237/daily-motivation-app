import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="Daily Motivation Generator", page_icon="💪", layout="centered")
st.title("💡 Daily Motivation Generator")
st.markdown("Feeling stuck or need a boost? Select your mood or situation and get an encouraging quote!")

moods = [
    "Feeling anxious", "Need focus", "Lack of motivation", "Feeling sad", "Self-doubt",
    "Facing a challenge", "Burnout", "Low energy", "Starting the day", "Ending the day"
]

selected_mood = st.selectbox("Choose your current situation or mood:", moods)

def generate_motivation(mood):
    prompt = f"""
    I am currently {mood.lower()}. Give me a short, original, and deeply encouraging motivational quote. 
    Keep it warm, personal, and human—not generic or robotic. Avoid clichés. Under 40 words.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or use "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a motivational coach."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.9,
            max_tokens=60
        )
        quote = response['choices'][0]['message']['content'].strip()
        return quote
    except Exception as e:
        return f"⚠️ Error: {e}"

if st.button("Generate Motivation ✨"):
    with st.spinner("Crafting your motivation..."):
        motivation = generate_motivation(selected_mood)
        st.success("Here's your quote:")
        st.markdown(f"> 🌟 *{motivation}*")
