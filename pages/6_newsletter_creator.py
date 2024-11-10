
# pages/6_newsletter_creator.py

import streamlit as st
from modules.tinyagi_utils import setup_tinyagi, display_configuration
from modules.ui_components import textarea_with_placeholder, input_with_placeholder, show_generated_content, loading_spinner, display_error, display_success
from modules.content_generator import generate_content
from modules.emojifier import emojify_text
import logging

def st_tags(label, text, key):
    # Simple implementation of a tags input using text input and splitting by commas
    tags = st.text_input(emojify_text(label), value='', key=key)
    tag_list = [tag.strip() for tag in tags.split(',') if tag.strip()]
    st.caption(emojify_text(text))
    return tag_list

def newsletter_creator(agent, plugin, tools):
    st.title(emojify_text(":newspaper: Newsletter Creator :newspaper:"))
    st.write(emojify_text("Automatically generate engaging newsletters for your audience."))

    niche = input_with_placeholder("Enter Newsletter Niche", "e.g., Technology, Health & Wellness")
    frequency = st.selectbox(emojify_text("Select Frequency"), ["Weekly", "Bi-weekly", "Monthly"])
    highlights = textarea_with_placeholder("Enter Highlights or Key Points", "List the main topics or news items")
    trending_topics = st_tags("Enter Trending Topics (comma-separated)", "Press enter to add more", key='trending_topics')

    # Advanced options
    with st.expander(emojify_text("Advanced Options")):
        include_images = st.checkbox(emojify_text("Include Image Suggestions"), value=False)
        personalized_greetings = st.checkbox(emojify_text("Include Personalized Greetings"), value=True)
        call_to_action = input_with_placeholder("Call-To-Action", "e.g., Visit our website, Subscribe now")

    if st.button(emojify_text("Generate Newsletter")):
        if not niche or not highlights:
            display_error("Please provide both niche and highlights.")
            return
        with loading_spinner("Generating newsletter..."):
            try:
                metadata = {
                    "frequency": frequency,
                    "include_images": include_images,
                    "personalized_greetings": personalized_greetings,
                    "call_to_action": call_to_action,
                }
                input_data = {
                    "prompt": f"Create a {frequency} newsletter for the niche: '{niche}'.",
                    "highlights": highlights,
                    "trending_topics": trending_topics,
                    "metadata": metadata
                }
                options = {"stream": False}
                response = generate_content(agent, plugin, tools, input_data, options)
                display_success("Newsletter Generated Successfully!")
                show_generated_content("Generated Newsletter", response)
                logging.info(f"Generated {frequency} newsletter for niche: {niche}")
            except Exception as e:
                display_error(f"Error generating newsletter: {str(e)}")
                logging.error(f"Error generating newsletter: {str(e)}")

def main():
    agent_system, agent, plugin, tools = setup_tinyagi()
    display_configuration(agent_system)
    newsletter_creator(agent, plugin, tools)

if __name__ == "__main__":
    main()
