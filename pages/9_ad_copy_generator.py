
# pages/9_ad_copy_generator.py

import streamlit as st
from modules.tinyagi_utils import setup_tinyagi, display_configuration
from modules.ui_components import textarea_with_placeholder, input_with_placeholder, show_generated_content, loading_spinner, display_error, display_success
from modules.content_generator import generate_content
from modules.emojifier import emojify_text
import logging

def ad_copy_generator(agent, plugin, tools):
    st.title(emojify_text(":rocket: Ad Copy Generator :rocket:"))
    st.write(emojify_text("Create compelling advertising copy tailored to specific platforms."))

    platform = st.selectbox(emojify_text("Select Advertising Platform"), ["Google Ads", "Facebook Ads", "LinkedIn Ads", "Instagram Ads", "Twitter Ads"])
    product_name = input_with_placeholder("Enter Product Name", "e.g., Eco-friendly Water Bottle")
    product_description = textarea_with_placeholder("Enter Product Description", "Provide a detailed description of the product")
    target_audience = input_with_placeholder("Enter Target Audience", "e.g., environmentally conscious consumers")

    # Advanced options
    with st.expander(emojify_text("Advanced Options")):
        ad_objective = st.selectbox(emojify_text("Ad Objective"), ["Brand Awareness", "Lead Generation", "Conversions", "Traffic"])
        call_to_action = input_with_placeholder("Call-To-Action", "e.g., Buy Now, Sign Up")
        include_emojis = st.checkbox(emojify_text("Include Emojis (where applicable)"), value=False)

    if st.button(emojify_text("Generate Ad Copy")):
        if not product_description:
            display_error("Please provide a product description.")
            return
        with loading_spinner("Generating ad copy..."):
            try:
                metadata = {
                    "platform": platform,
                    "product_name": product_name,
                    "target_audience": target_audience,
                    "ad_objective": ad_objective,
                    "call_to_action": call_to_action,
                    "include_emojis": include_emojis,
                }
                input_data = {
                    "prompt": f"Create compelling ad copy for {platform} for the product '{product_name}'.",
                    "product_description": product_description,
                    "metadata": metadata
                }
                options = {"stream": False}
                response = generate_content(agent, plugin, tools, input_data, options)
                display_success("Ad Copy Generated Successfully!")
                show_generated_content("Generated Ad Copy", response)
                logging.info(f"Generated ad copy for platform: {platform}")
            except Exception as e:
                display_error(f"Error generating ad copy: {str(e)}")
                logging.error(f"Error generating ad copy: {str(e)}")

def main():
    agent_system, agent, plugin, tools = setup_tinyagi()
    display_configuration(agent_system)
    ad_copy_generator(agent, plugin, tools)

if __name__ == "__main__":
    main()
