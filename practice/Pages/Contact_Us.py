import pandas
import streamlit as st
from send_email import send_email
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
st.header("Contact Us")

with st.form(key="email_form"):
    df = pandas.read_csv(BASE_DIR / "topics.csv")



    user_email = st.text_input("Your email address")
    topic_email = st.selectbox("Topic",df["topic"].tolist())
    raw_message = st.text_area("Your message")

    message = f"""\
Subject: New email from {user_email}
From: {user_email}
{topic_email}
{raw_message}
"""

    button = st.form_submit_button("Submit")

    if button:
        send_email(message)
        st.info("Your email was sent successfully!")