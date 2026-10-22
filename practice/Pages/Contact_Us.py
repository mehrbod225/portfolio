import pandas
import streamlit as st
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR / "practice"))

from send_email import send_email

st.header("Contact Us")

with st.form(key="email_form"):
    df = pandas.read_csv(BASE_DIR / "practice" / "topics.csv")

    user_email = st.text_input("Your email address")
    topic_email = st.selectbox("Topic", df["topic"].tolist())
    raw_message = st.text_area("Your message")

    message = f"""\
Subject: New email from {user_email}
From: {user_email}
Topic: {topic_email}
{raw_message}
"""

    button = st.form_submit_button("Submit")

    if button:
        send_email(message)
        st.info("Your email was sent successfully!")