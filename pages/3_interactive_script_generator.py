
# pages/3_interactive_script_generator.py

import streamlit as st
from modules.tinyagi_utils import setup_tinyagi, display_configuration
from modules.ui_components import textarea_with_placeholder, show_generated_content, loading_spinner, display_error, display_success, input_with_placeholder
from modules.content_generator import generate_content
from modules.emojifier import emojify_text
import logging

def interactive_script_generator(agent, plugin, tools):
    st.title(emojify_text(":clapper: Interactive Script Generator :clapper:"))
    st.write(emojify_text("Create scripts for podcasts, videos, or interviews."))

    script_type = st.selectbox(emojify_text("Script Type"), ["Podcast", "YouTube Video", "Interview", "Webinar", "Tutorial"])
    style = st.multiselect(emojify_text("Style"), ["Informative", "Casual", "Formal", "Humorous", "Dramatic"], default=["Informative"])
    target_audience = st.text_input(emojify_text("Target Audience"), placeholder="e.g., beginners, professionals")
    duration = st.slider(emojify_text("Duration (minutes)"), min_value=1, max_value=180, value=30)
    prompt = textarea_with_placeholder("Enter Script Prompt", "Provide a brief description or idea for the script")

    # Advanced options
    with st.expander(emojify_text("Advanced Options")):
        include_visuals = st.checkbox(emojify_text("Include Visual Descriptions"), value=False)
        number_of_speakers = st.number_input(emojify_text("Number of Speakers"), min_value=1, max_value=10, value=2)
        language = st.selectbox(emojify_text("Language"), ["English", "Spanish", "French", "German", "Chinese"])

    if st.button(emojify_text("Generate Script")):
        if not prompt:
            display_error("Please provide a script prompt.")
            return
        with loading_spinner("Generating script..."):
            try:
                metadata = {
                    "style": style,
                    "target_audience": target_audience,
                    "duration": duration,
                    "include_visuals": include_visuals,
                    "number_of_speakers": number_of_speakers,
                    "language": language,
                }
                input_data = {
                    "prompt": f"Generate a {script_type} script based on the following prompt: {prompt}",
                    "metadata": metadata
                }
                options = {"stream": False}
                response = generate_content(agent, plugin, tools, input_data, options)
                display_success("Script Generated Successfully!")
                show_generated_content("Generated Script", response)
                logging.info(f"Generated {script_type} script with prompt: {prompt}")
            except Exception as e:
                display_error(f"Error generating script: {str(e)}")
                logging.error(f"Error generating script: {str(e)}")

def main():
    agent_system, agent, plugin, tools = setup_tinyagi()
    display_configuration(agent_system)
    interactive_script_generator(agent, plugin, tools)

if __name__ == "__main__":
    main()
