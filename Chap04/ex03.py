# builds a demo application to use the utility features of Streamlit


import streamlit as st

# Setting the page config
st.set_page_config(page_title="My Awesome App", page_icon=":tada:", layout="wide")


# Displaying code and its output
# echo : Displays text as a code block
with st.echo():
    # This code will be shown and executed
    st.write("This line will be printed and its code displayed.")


# Showing help information for a Streamlit function
# help : Prints help results for any object
st.help(st.sidebar)