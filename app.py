import streamlit as st

from service  import get_career_advice


st.set_page_config(
    page_title="Career Advisor Chatbot",
    page_icon="📊",
    layout="centered"
)

st.markdown("""
<h1 style='text-align: center;
background: linear-gradient(to right,
red, orange, yellow, green, cyan, blue, violet);
-webkit-background-clip: text;
-webkit-text-fill-color: transparent;
font-size: 55px;
font-weight: bold;'>

👤 AI Career Advisor Chatbot

</h1>
""", unsafe_allow_html=True)

user_input = st.text_input(
    "Enter your question:"
)

if st.button("Ask"):

    if user_input:

        response = get_career_advice(user_input)

        st.write(response)