import streamlit as st
st.set_page_config()

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Mehrbod Amin")
    #تو خونه هرچیزی مه درمورد خودت میتونی بنویس
    #بنویس  و بعدش رو نتونستم بخونم شرمنده
    #منه آینده که میخوای مشقاتو آخر وقت بنویسی
    content="""
    Hi my name is Mehrbod
    i'm python programmer student and i love to study python and AI thing to bright my future.
    i'm only 15 years old and i study in Ghanbari school which is awful my last school (Majid Morshed) was better than this one"""
    st.write(content)
content2 = """
below you can see other things i built feel free to contact me
"""
st.write(content2)
