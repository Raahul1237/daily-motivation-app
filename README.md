# 💡 Daily Motivation Generator

This is a simple Streamlit web app that generates short, personalized motivational quotes based on your current mood or situation. Whether you're feeling anxious, low on energy, or just need a small push to focus — this app is here for you.

Features: Choose your current mood or situation, get a unique motivational quote, built with Python, Streamlit, and Hugging Face’s free API. Clean, user-friendly interface.

How to Run the App Locally:
1. Clone the Repository:
git clone https://github.com/yourusername/daily-motivation-app.git
cd daily-motivation-app

2. (Optional) Set Up a Virtual Environment:
python3 -m venv venv
source venv/bin/activate  (for macOS/Linux)
venv\Scripts\activate     (for Windows)

3. Install Dependencies:
pip install -r requirements.txt

4. Add Your Hugging Face API Token:
Create a file named .env and paste:
HUGGINGFACE_TOKEN=hf_your_actual_token_here
(Never share your .env or token publicly.)

5. Run the App:
streamlit run app.py
Visit http://localhost:8501 in your browser to use the app.

Tech Stack: Python, Streamlit, Hugging Face Transformers API, dotenv

Folder Structure:
daily-motivation-app/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env  # not uploaded to GitHub

Sensitive Files (Never Upload): .env (contains your private API token), venv/ (your local Python environment)

Future Improvements: Shareable quotes (copy or download), more moods & quote categories, online deployment (Streamlit Cloud or Hugging Face Spaces)

License: This project is open source under the MIT License.

Made with ❤️ by Raahul.
