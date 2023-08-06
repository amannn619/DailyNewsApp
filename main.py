import streamlit as st
import send_news
st.title("Get News")

with st.form(key = "registration", clear_on_submit=True):
    email = st.text_input(label="Email", placeholder="Enter your email...")
    keyword = st.text_input(label = "Keyword", placeholder="Whatever you want to read about...")
    submit = st.form_submit_button(label = "Get News")
    if submit:
        if keyword=="":
            keyword = "tesla"
        message = send_news.create_mail_content(keyword)
        print(message)
        send_news.send_news(email, message)