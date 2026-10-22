import streamlit as st
import runpy
from pathlib import Path

BASE_DIR = Path(__file__).parent

st.set_page_config(
    page_title="The Best Company",
    layout="wide"
)

def home():
    import pandas

    st.title("The Best Company")
    st.write("""
    Welcome to our company!

    Meet our team and learn about the people
    who work together to make great things.
    """)

    st.header("Our Team")

    df = pandas.read_csv(BASE_DIR / "data2.csv")
    col1, col2, col3 = st.columns(3)

    for col, start in zip([col1, col2, col3], [0, 4, 8]):
        with col:
            for _, row in df[start:start + 4].iterrows():
                st.header(row["first name"] + " " + row["last name"])
                st.write(row["role"])
                st.image(
                    str(BASE_DIR / "images2" / row["image"]),
                    width=200
                )

def contact():
    runpy.run_path(str(BASE_DIR / "pages" / "1_Contact_Us.py"))

pg = st.navigation([
    st.Page(home, title="Home", default=True),
    st.Page(contact, title="Contact Us")
])

pg.run()
