
import streamlit as st
from utils.config_handler import load_config, save_config
import json
import logging

logger = logging.getLogger(__name__)

def configuration_builder():
    st.header("🛠️ Configuration Builder")

    config = load_config()

    if st.checkbox("Load Existing Configuration"):
        st.subheader("Existing Configuration")
        st.json(config)
    
    st.markdown("### Edit Configuration")
    with st.form("edit_config_form"):
        config_json = st.text_area("Configuration (JSON)", json.dumps(config, indent=2), height=400)
        submit = st.form_submit_button("Save Configuration")

        if submit:
            try:
                updated_config = json.loads(config_json)
                save_config(updated_config)
                st.success("Configuration saved successfully.")
                logger.info("Configuration updated via Configuration Builder.")
            except json.JSONDecodeError:
                st.error("Invalid JSON format. Please correct and try again.")

    st.markdown("### Download Configuration")
    if st.button("Download agent_config.json"):
        config_str = json.dumps(config, indent=2)
        st.download_button(
            label="Download Configuration",
            data=config_str,
            file_name='agent_config.json',
            mime='application/json'
        )
    
    st.markdown("### Upload Configuration")
    uploaded_file = st.file_uploader("Upload a new agent_config.json", type=["json"])
    if uploaded_file is not None:
        try:
            uploaded_config = json.load(uploaded_file)
            save_config(uploaded_config)
            st.success("Configuration uploaded and saved successfully.")
            logger.info("Configuration uploaded via Configuration Builder.")
        except json.JSONDecodeError:
            st.error("Invalid JSON format in the uploaded file.")
