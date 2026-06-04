# 🤖 AI Career Advisor Chatbot

## 📌 Project Overview

AI Career Advisor Chatbot is a Streamlit-based Generative AI application that provides career guidance, skill recommendations, learning roadmaps, resume improvement suggestions, and interview preparation tips using Google's Gemini API.

The chatbot is designed to help students, fresh graduates, and professionals make informed career decisions through an interactive conversational interface.

---

# 🚀 Problem Statement

Many students and job seekers struggle with:

- Choosing the right career path
- Understanding industry-required skills
- Creating effective learning roadmaps
- Preparing for technical and HR interviews
- Improving resumes according to industry standards

Traditional career guidance often requires mentors, counselors, or extensive research, which may not always be accessible.

---

# 🎯 Objective

The objective of this project is to build an AI-powered career guidance assistant that can:

- Provide career-related advice instantly
- Recommend relevant technical and soft skills
- Generate structured learning roadmaps
- Offer interview preparation guidance
- Suggest resume improvement strategies
- Deliver personalized responses through natural language conversations

---

# 🛠️ Tech Stack

## Frontend
- Streamlit

## Backend
- Python

## Generative AI
- Google Gemini 2.5 Flash

## Environment Management
- Python Virtual Environment (venv)
- python-dotenv

## Logging
- Python Logging Module

## API Integration
- Google Generative AI SDK

---

# ✨ Features

## Career Guidance
- Career path recommendations
- Role-based guidance

## Skill Recommendations
- Technical skills
- Soft skills
- Industry-specific skills

## Learning Roadmaps
- Step-by-step learning plans
- Structured progression

## Interview Preparation
- Technical interview tips
- HR interview guidance
- Communication improvement tips

---

# 📂 Project Structure

```text
AI-Career-Advisor/
│
├── app.py
├── service.py
├── .env
├── requirements.txt
├── app.log
└── README.md
```

---
# 🏗️ Working Flow

1. User enters a career-related question.
2. Streamlit captures the input.
3. Query is sent to the service layer.
4. Gemini API processes the request.
5. Structured response is generated.
6. Response is displayed in the chatbot UI.
7. User query and system logs are stored in app.log.

---

# ⚠️ Challenges Faced

### 1. Prompt Engineering
Creating prompts that consistently generate structured career advice.

### 2. Session Management
Maintaining conversation history using Streamlit Session State.

### 3. API Error Handling
Managing failures and unexpected API responses gracefully.

### 4. Security
Protecting API keys using environment variables.

---

# 🎯 Outcomes

- Developed an AI-powered career guidance chatbot.
- Integrated Google Gemini API into a real-world application.
- Learned prompt engineering techniques.
- Implemented session management in Streamlit.
- Added logging for monitoring and debugging.
- Improved understanding of Generative AI application development.

---

---

