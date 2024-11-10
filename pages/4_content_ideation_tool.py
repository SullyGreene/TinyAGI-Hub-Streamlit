
# pages/4_content_ideation_tool.py

import streamlit as st
from modules.tinyagi_utils import setup_tinyagi, display_configuration
from modules.ui_components import input_with_placeholder, show_generated_content, loading_spinner, display_error, display_success
from modules.content_generator import generate_content
from modules.emojifier import emojify_text
import logging

def content_ideation_tool(agent, plugin, tools):
    st.title(emojify_text(":bulb: Content Ideation Tool :bulb:"))
    st.write(emojify_text("Brainstorm content ideas for your next project."))

    topic = input_with_placeholder("Enter Topic or Trend", "e.g., renewable energy, AI in healthcare")
    content_types = st.multiselect(emojify_text("Content Types"), ["Blog Posts", "Articles", "Social Media Posts", "Videos", "Podcasts"], default=["Blog Posts"])
    number_of_ideas = st.slider(emojify_text("Number of Ideas"), min_value=1, max_value=50, value=5)

    # Advanced options
    with st.expander(emojify_text("Advanced Options")):
        target_audience = st.text_input(emojify_text("Target Audience"), placeholder="e.g., teenagers, professionals")
        keywords = st.text_input(emojify_text("Keywords to Include"), placeholder="e.g., sustainability, innovation")
        tone = st.selectbox(emojify_text("Tone"), ["Informative", "Persuasive", "Entertaining", "Educational"])

    if st.button(emojify_text("Generate Content Ideas")):
        if not topic:
            display_error("Please provide a topic or trend.")
            return
        with loading_spinner("Generating content ideas..."):
            try:
                metadata = {
                    "content_types": content_types,
                    "target_audience": target_audience,
                    "keywords": keywords,
                    "tone": tone,
                }
                input_data = {
                    "prompt": f"Generate {number_of_ideas} content ideas for the topic: '{topic}'.",
                    "metadata": metadata
                }
                options = {"stream": False}
                response = generate_content(agent, plugin, tools, input_data, options)
                display_success("Content Ideas Generated Successfully!")
                show_generated_content("Generated Content Ideas", response)
                logging.info(f"Generated {number_of_ideas} content ideas for topic: {topic}")
            except Exception as e:
                display_error(f"Error generating content ideas: {str(e)}")
                logging.error(f"Error generating content ideas: {str(e)}")

def main():
    agent_system, agent, plugin, tools = setup_tinyagi()
    display_configuration(agent_system)
    content_ideation_tool(agent, plugin, tools)

if __name__ == "__main__":
    main()
