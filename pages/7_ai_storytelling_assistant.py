
# pages/7_ai_storytelling_assistant.py

import streamlit as st
from modules.tinyagi_utils import setup_tinyagi, display_configuration
from modules.ui_components import textarea_with_placeholder, show_generated_content, loading_spinner, display_error, display_success, input_with_placeholder
from modules.content_generator import generate_content
from modules.emojifier import emojify_text
import logging

def ai_storytelling_assistant(agent, plugin, tools):
    st.title(emojify_text(":book: AI Storytelling Assistant :book:"))
    st.write(emojify_text("Generate story elements to inspire your writing."))

    genre = st.selectbox(emojify_text("Select Genre"), ["Fantasy", "Sci-Fi", "Mystery", "Romance", "Horror", "Adventure", "Historical"])
    style = st.multiselect(emojify_text("Select Style"), ["Descriptive", "Dialogue-heavy", "Narrative", "First-person", "Third-person"], default=["Narrative"])
    target_audience = st.text_input(emojify_text("Enter Target Audience"), placeholder="e.g., young adults, children")
    prompt = textarea_with_placeholder("Enter Story Prompt", "Provide a basic idea or theme for your story")

    # Advanced options
    with st.expander(emojify_text("Advanced Options")):
        include_character_profiles = st.checkbox(emojify_text("Include Character Backstories"), value=True)
        include_plot_twists = st.checkbox(emojify_text("Include Plot Twists"), value=False)
        desired_length = st.slider(emojify_text("Desired Length (words)"), min_value=500, max_value=5000, value=1000, step=100)

    if st.button(emojify_text("Generate Story Elements")):
        if not prompt:
            display_error("Please provide a story prompt.")
            return
        with loading_spinner("Generating story elements..."):
            try:
                metadata = {
                    "genre": genre,
                    "style": style,
                    "target_audience": target_audience,
                    "include_character_profiles": include_character_profiles,
                    "include_plot_twists": include_plot_twists,
                    "desired_length": desired_length,
                }
                input_data = {
                    "prompt": f"Generate story elements based on the following prompt: {prompt}",
                    "metadata": metadata
                }
                options = {"stream": False}
                response = generate_content(agent, plugin, tools, input_data, options)
                display_success("Story Elements Generated Successfully!")
                show_generated_content("Generated Story Elements", response)
                logging.info(f"Generated story elements for genre: {genre} with prompt: {prompt}")
            except Exception as e:
                display_error(f"Error generating story elements: {str(e)}")
                logging.error(f"Error generating story elements: {str(e)}")

def main():
    agent_system, agent, plugin, tools = setup_tinyagi()
    display_configuration(agent_system)
    ai_storytelling_assistant(agent, plugin, tools)

if __name__ == "__main__":
    main()
