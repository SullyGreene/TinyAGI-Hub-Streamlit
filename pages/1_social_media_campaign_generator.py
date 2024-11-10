
# pages/1_social_media_campaign_generator.py

import streamlit as st
from modules.tinyagi_utils import setup_tinyagi, display_configuration
from modules.ui_components import show_generated_content, loading_spinner, display_error, display_success, input_with_placeholder
from modules.content_generator import generate_content
from modules.emojifier import emojify_text
import logging

def social_media_campaign_generator(agent, plugin, tools):
    st.title(emojify_text(":megaphone: Social Media Campaign Generator :megaphone:"))
    st.write(emojify_text("Create comprehensive social media campaigns across multiple platforms."))

    platforms = ["Instagram", "Twitter", "LinkedIn", "Facebook", "TikTok"]
    selected_platforms = st.multiselect(emojify_text("Select Platforms"), platforms, default=platforms)
    campaign_theme = input_with_placeholder("Campaign Theme or Topic", "Enter the main theme of your campaign")
    scheduling = st.select_slider(emojify_text("Select Scheduling Frequency"), options=["Daily", "Weekly", "Monthly"], value="Weekly")

    start_date = st.date_input(emojify_text("Campaign Start Date"))
    end_date = st.date_input(emojify_text("Campaign End Date"))

    # Advanced options in an expander
    with st.expander(emojify_text("Advanced Options")):
        include_images = st.checkbox(emojify_text("Include Image Suggestions"), value=True)
        include_hashtags = st.checkbox(emojify_text("Include Hashtags"), value=True)
        tone_of_voice = st.selectbox(emojify_text("Tone of Voice"), ["Professional", "Casual", "Humorous", "Inspirational"])

    if st.button(emojify_text("Generate Campaign")):
        if not campaign_theme:
            display_error("Please provide a campaign theme or topic.")
            return
        with loading_spinner("Generating social media campaign..."):
            try:
                metadata = {
                    "scheduling": scheduling,
                    "start_date": str(start_date),
                    "end_date": str(end_date),
                    "include_images": include_images,
                    "include_hashtags": include_hashtags,
                    "tone_of_voice": tone_of_voice,
                }
                input_data = {
                    "prompt": f"Create a social media campaign for the topic: '{{campaign_theme}}' targeting platforms: {{', '.join(selected_platforms)}}.",
                    "metadata": metadata
                }
                options = {"stream": False}
                response = generate_content(agent, plugin, tools, input_data, options)
                display_success("Campaign Generated Successfully!")
                show_generated_content("Generated Campaign", response)
                logging.info(f"Generated social media campaign with theme: {{campaign_theme}}")
            except Exception as e:
                display_error(f"Error generating campaign: {{str(e)}}")
                logging.error(f"Error generating campaign: {{str(e)}}")

def main():
    agent_system, agent, plugin, tools = setup_tinyagi()
    display_configuration(agent_system)
    social_media_campaign_generator(agent, plugin, tools)

if __name__ == "__main__":
    main()
