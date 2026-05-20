import streamlit as st
import google.generativeai as genai
import os
import logging

from dotenv import load_dotenv


load_dotenv() 
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
) 


genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

SYSTEM_PROMPT = """
You are an AI Career Advisor chatbot.

Responsibilities:
- Provide career guidance
- Suggest technical skills
- Give learning roadmap
- Help with interview preparation
- Improve resumes

Rules:
- Answer only career-related questions
- Keep answers structured
- Be professional and concise
- Keep response under 250 words

Formatting Rules:
1. Learning roadmap MUST be in numbered steps.
2. Interview preparation tips MUST be in bullet points.
3. Skills section should be comma-separated.
4. Use clear headings.
"""

def get_career_advice(user_query):

    prompt = f"""
    {SYSTEM_PROMPT}

    User Question:
    {user_query}

    Give response in this format:

    1. Career Advice
    2. Required Skills
    3. Learning Roadmap
    4. Interview Tips
    """

    try:

        logging.info(f"User Query: {user_query}")

        response = model.generate_content(prompt)

        logging.info("Gemini API Success")

        return response.text

    except Exception as e:

        logging.error(f"Error: {str(e)}")

        return "Sorry, something went wrong."

st.set_page_config(
    page_title="AI Career Advisor",
    page_icon="🤖",
    layout="centered"
)

# =========================================
# TITLE
# =========================================

st.title("🤖 AI Career Advisor")
st.caption("Production-grade chatbot using Gemini API")

# =========================================
# CHAT HISTORY
# =========================================

if "messages" not in st.session_state:
    st.session_state.messages = []

# display old messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# =========================================
# USER INPUT
# =========================================

user_input = st.chat_input(
    "Ask your career question..."
)

# =========================================
# PROCESS INPUT
# =========================================

if user_input:

    # show user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # loading spinner
    with st.spinner("Thinking..."):

        bot_response = get_career_advice(
            user_input
        )

    # show assistant response
    with st.chat_message("assistant"):
        st.markdown(bot_response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })