import streamlit as st


# Define the callback function
def toggle_message():
    # 解释下面的代码，
    # 如果 'show_message' 不在 session_state 中，则初始化为 False
    # 如果在 session_state 中，则切换其值
    # 这样可以在每次点击按钮时切换消息的显示状态
    if 'show_message' not in st.session_state:
        st.session_state.show_message = False
    st.session_state.show_message = not st.session_state.show_message


# Create a button that toggles the message
st.button("Toggle Message", on_click=toggle_message)


# Conditionally display the message based on the session state
if st.session_state.get('show_message', False):
    st.write("Hello, this is a message that can be toggled!")