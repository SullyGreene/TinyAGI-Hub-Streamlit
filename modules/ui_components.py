
# modules/ui_components.py

import streamlit as st
from modules.emojifier import emojify_text

def show_generated_content(title, content):
    st.subheader(emojify_text(title))
    with st.expander(emojify_text("Show/Hide Content"), expanded=True):
        st.write(emojify_text(content))

def input_with_placeholder(label, placeholder, key=None):
    return st.text_input(emojify_text(label), placeholder=emojify_text(placeholder), key=key)

def textarea_with_placeholder(label, placeholder, key=None):
    return st.text_area(emojify_text(label), placeholder=emojify_text(placeholder), key=key)

def loading_spinner(text):
    return st.spinner(emojify_text(text))

def display_error(message):
    st.error(emojify_text(message))

def display_success(message):
    st.success(emojify_text(message))
