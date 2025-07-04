import streamlit as st

# Callback to process form submission
def process_form():
    user_name = st.session_state.user_name
    user_age = st.session_state.user_age
    st.write(f"Hello {user_name}, you are {user_age} years old!")

# Define a form with two input fields and a submit button
with st.form(key='user_form', clear_on_submit=True):
    st.text_input("Enter your name", key='user_name')
    st.number_input("Enter your age", min_value=0, max_value=120, key='user_age')
    submit_button = st.form_submit_button(label='Submit', on_click=process_form)