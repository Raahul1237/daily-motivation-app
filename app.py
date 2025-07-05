import streamlit as st
import requests
import os
from dotenv import load_dotenv

# Load Hugging Face token from .env
load_dotenv()
HF_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

# Streamlit UI
st.set_page_config(page_title="Daily Motivation Generator", page_icon="💪", layout="centered")
st.title("💡 Daily Motivation Generator")
st.markdown("Feeling stuck or need a boost? Select your mood or situation and get an encouraging quote!")

# Mood dropdown
moods = [
    "Feeling anxious", "Need focus", "Lack of motivation", "Feeling sad", "Self-doubt",
    "Facing a challenge", "Burnout", "Low energy", "Starting the day", "Ending the day"
]
selected_mood = st.selectbox("Choose your current situation or mood:", moods)

# Use GPT-2 (public model) to generate motivational quotes
def generate_motivation(mood):
    prompt = f"Motivational quote for someone who is {mood.lower()}:"

    try:
        response = requests.post(
            "https://api-inference.huggingface.co/models/gpt2",
            headers={"Authorization": f"Bearer {HF_TOKEN}"},
            json={"inputs": prompt, "parameters": {"max_new_tokens": 40}}
        )

        if response.status_code == 200:
            return response.json()[0]["generated_text"].replace(prompt, "").strip()
        elif response.status_code == 401:
            return "⚠️ Invalid Hugging Face token. Check your `.env` file."
        elif response.status_code == 403:
            return "⚠️ You don't have permission to use this model. Try another one."
        else:
            return f"⚠️ API Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"⚠️ Error: {e}"

# Display result on button click
if st.button("Generate Motivation ✨"):
    with st.spinner("Crafting your motivation..."):
        quote = generate_motivation(selected_mood)
        st.success("Here's your quote:")
        st.markdown(f"> 🌟 *{quote}*")
