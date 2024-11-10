
# pages/5_seo_content_optimizer.py

import streamlit as st
from modules.tinyagi_utils import setup_tinyagi, display_configuration
from modules.ui_components import textarea_with_placeholder, show_generated_content, loading_spinner, display_error, display_success
from modules.content_generator import generate_content
from modules.emojifier import emojify_text
import logging

def seo_content_optimizer(agent, plugin, tools):
    st.title(emojify_text(":mag: SEO Content Optimizer :mag:"))
    st.write(emojify_text("Enhance your content to rank higher in search engines."))

    content_type = st.selectbox(emojify_text("Select Content Type"), ["Blog Post", "Article", "Web Page", "Product Description"])
    content = textarea_with_placeholder("Enter Your Content", "Paste your existing content here")
    keywords = st.text_input(emojify_text("Enter Keywords (comma-separated)"), placeholder="e.g., AI, machine learning, automation")

    # Advanced options
    with st.expander(emojify_text("Advanced Options")):
        target_keyword = st.text_input(emojify_text("Primary Target Keyword"), placeholder="e.g., artificial intelligence")
        keyword_density = st.slider(emojify_text("Desired Keyword Density (%)"), min_value=0.5, max_value=5.0, value=1.0, step=0.1)
        tone = st.selectbox(emojify_text("Tone of Content"), ["Informative", "Persuasive", "Friendly", "Professional"])

    if st.button(emojify_text("Optimize Content for SEO")):
        if not content:
            display_error("Please provide the content to optimize.")
            return
        with loading_spinner("Optimizing content for SEO..."):
            try:
                metadata = {
                    "keywords": keywords,
                    "target_keyword": target_keyword,
                    "keyword_density": keyword_density,
                    "tone": tone,
                }
                input_data = {
                    "prompt": f"Optimize the following {content_type} for SEO.",
                    "content": content,
                    "metadata": metadata
                }
                options = {"stream": False}
                response = generate_content(agent, plugin, tools, input_data, options)
                display_success("Content Optimized Successfully!")
                show_generated_content("Optimized Content", response)
                logging.info(f"Optimized {content_type} for SEO with keywords: {keywords}")
            except Exception as e:
                display_error(f"Error optimizing content: {str(e)}")
                logging.error(f"Error optimizing content: {str(e)}")

def main():
    agent_system, agent, plugin, tools = setup_tinyagi()
    display_configuration(agent_system)
    seo_content_optimizer(agent, plugin, tools)

if __name__ == "__main__":
    main()
