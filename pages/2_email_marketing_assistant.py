
# pages/2_email_marketing_assistant.py

import streamlit as st
from modules.tinyagi_utils import setup_tinyagi, display_configuration
from modules.ui_components import input_with_placeholder, textarea_with_placeholder, show_generated_content, loading_spinner, display_error, display_success
from modules.content_generator import generate_content
from modules.emojifier import emojify_text
import logging

def email_marketing_assistant(agent, plugin, tools):
    st.title(emojify_text(":email: Email Marketing Assistant :email:"))
    st.write(emojify_text("Generate personalized email campaigns with ease."))

    col1, col2 = st.columns(2)
    with col1:
        subject = input_with_placeholder("Email Subject Line", "Enter the email subject")
    with col2:
        cta = input_with_placeholder("Call-To-Action (CTA)", "Enter the call-to-action")

    body = textarea_with_placeholder("Email Body Content", "Enter the main content of the email")

    # Advanced options in an expander
    with st.expander(emojify_text("Advanced Options")):
        personalization = st.checkbox(emojify_text("Include Personalization Tags"), value=True)
        tone = st.select_slider(emojify_text("Tone of the Email"), options=["Formal", "Friendly", "Humorous"], value="Friendly")
        preview_text = input_with_placeholder("Preview Text", "Enter preview text for the email")

    if st.button(emojify_text("Generate Email Campaign")):
        if not subject or not body:
            display_error("Please provide both subject line and body content.")
            return
        with loading_spinner("Generating email campaign..."):
            try:
                metadata = {
                    "cta": cta,
                    "personalization": personalization,
                    "tone": tone,
                    "preview_text": preview_text,
                }
                input_data = {
                    "prompt": f"Create an email campaign with the following details:\nSubject: {subject}\nBody: {body}",
                    "metadata": metadata
                }
                options = {"stream": False}
                response = generate_content(agent, plugin, tools, input_data, options)
                display_success("Email Campaign Generated Successfully!")
                show_generated_content("Generated Email", response)
                logging.info(f"Generated email campaign with subject: {subject}")
            except Exception as e:
                display_error(f"Error generating email campaign: {str(e)}")
                logging.error(f"Error generating email campaign: {str(e)}")

def main():
    agent_system, agent, plugin, tools = setup_tinyagi()
    display_configuration(agent_system)
    email_marketing_assistant(agent, plugin, tools)

if __name__ == "__main__":
    main()
