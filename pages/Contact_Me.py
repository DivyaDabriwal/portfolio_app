import streamlit as st

st.title('Contact Me')

with st.form("my_form"):
    email_address = st.text_input(label='Your email address', key='email_address')
    raw_message = st.text_area(label='Your message', key='message')
    submit_button = st.form_submit_button('Submit')

if submit_button:
    with st.spinner('Wait for it...'):
        message = f"""Subject: Mail from Portfolio App\n
        {raw_message}\n
        From: {email_address}"""