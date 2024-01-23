import streamlit as st
from send_email import send_email

st.header("Contact List")

with st.form(key="form"):
    name = st.text_input(label="Your Name")
    email = st.text_input(label="Your Email Address")
    phone = st.text_input(label="Your Phone Number")
    subject = st.text_input(label="Subject")
    message = st.text_area(label="Your Message")
    
    submit_button = st.form_submit_button(label="Submit")
    
    if submit_button:
        if name and email and phone and subject and message:
            full_message = f"Name: {name}\nPhone: {phone}\nSubject: {subject}\n\n{message}"
            send_email(full_message)
            st.success("Your message has been sent.")
        else:
            st.error("Please fill in all fields before submitting.")
