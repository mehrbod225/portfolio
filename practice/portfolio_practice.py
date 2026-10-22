import pandas
import streamlit as st

st.set_page_config(
    page_title="The Best Company",
    layout="wide"
)

st.title("The Best Company")

content = """
Welcome to our company!

Meet our team and learn about the people
who work together to make great things.
"""

st.write(content)

st.header("Our Team")
from pathlib import Path
csv_file = Path(__file__).parent / "data2.csv"

df = pandas.read_csv(csv_file)

col1, col2, col3 = st.columns(3)

with col1:
    for index, row in df[:4].iterrows():

        st.header(row["first name"] + " " + row["last name"])

        st.write(row["role"])

        st.image("images2/" + row["image"], width=200)
with col3:
    for index, row in df[4:8].iterrows():
        st.header(row["first name"] + " " + row["last name"])

        st.write(row["role"])

        st.image("images2/" + row["image"], width=200)

with col2:
    for index, row in df[8:].iterrows():

        st.header(row["first name"] + " " + row["last name"])
st.write("TEST - Portfolio page is running")
        st.write(row["role"])

        st.image("images2/" + row["image"], width=200)

