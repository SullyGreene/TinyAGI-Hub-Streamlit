
# pages/8_academic_article_summary_tool.py

import streamlit as st
from modules.tinyagi_utils import setup_tinyagi, display_configuration
from modules.ui_components import input_with_placeholder, show_generated_content, loading_spinner, display_error, display_success, textarea_with_placeholder
from modules.content_generator import generate_content
from modules.emojifier import emojify_text
import logging

def academic_article_summary_tool(agent, plugin, tools):
    st.title(emojify_text(":mortar_board: Academic Article Summary Tool :mortar_board:"))
    st.write(emojify_text("Summarize academic papers quickly and efficiently."))

    paper_title = input_with_placeholder("Enter Academic Paper Title", "e.g., The impact of climate change on marine life")
    author = input_with_placeholder("Enter Author Name(s)", "e.g., John Doe, Jane Smith")
    abstract = textarea_with_placeholder("Enter Abstract (Optional)", "Paste the abstract if available")

    # Advanced options
    with st.expander(emojify_text("Advanced Options")):
        include_key_takeaways = st.checkbox(emojify_text("Include Key Takeaways"), value=True)
        include_references = st.checkbox(emojify_text("Include References"), value=False)
        summary_length = st.select_slider(emojify_text("Summary Length"), options=["Short", "Medium", "Long"], value="Medium")

    if st.button(emojify_text("Generate Summary")):
        if not paper_title and not abstract:
            display_error("Please provide either the paper title or the abstract.")
            return
        with loading_spinner("Generating summary..."):
            try:
                metadata = {
                    "author": author,
                    "include_key_takeaways": include_key_takeaways,
                    "include_references": include_references,
                    "summary_length": summary_length,
                }
                input_data = {
                    "prompt": f"Summarize the academic paper titled '{paper_title}' authored by {author}.",
                    "abstract": abstract,
                    "metadata": metadata
                }
                options = {"stream": False}
                response = generate_content(agent, plugin, tools, input_data, options)
                display_success("Summary Generated Successfully!")
                show_generated_content("Generated Summary", response)
                logging.info(f"Generated summary for paper: {paper_title} by {author}")
            except Exception as e:
                display_error(f"Error generating summary: {str(e)}")
                logging.error(f"Error generating summary: {str(e)}")

def main():
    agent_system, agent, plugin, tools = setup_tinyagi()
    display_configuration(agent_system)
    academic_article_summary_tool(agent, plugin, tools)

if __name__ == "__main__":
    main()
