import streamlit as st
from utils.config_handler import load_config, save_config
import json
import logging

logger = logging.getLogger(__name__)

def manage_modules():
    st.header("🔧 Manage Modules")

    # Load current configuration
    config = load_config()

    modules = config.get('modules', [])

    # Display existing modules
    if modules:
        st.subheader("Existing Modules")
        for module in modules:
            st.write(f"**Name:** {module.get('name')}")
            st.write(f"**Module Path:** {module.get('module')}")
            st.write(f"**Source:** {module.get('source', 'local')}")
            if module.get('source') == 'github':
                st.write(f"**Repo URL:** {module.get('repo_url')}")
            st.write("---")
    else:
        st.info("No modules configured yet.")

    # Section to add a new module
    st.markdown("### Add New Module")
    with st.form("add_module_form"):
        module_name = st.text_input("Module Name", "")
        module_path = st.text_input("Module Path", "")
        source = st.selectbox("Source", ["local", "github"])
        repo_url = st.text_input("GitHub Repo URL (if applicable)", "")
        config_json = st.text_area("Configuration (JSON)", "{}")
        submit = st.form_submit_button("Add Module")

        if submit:
            if not module_name or not module_path:
                st.error("Module Name and Module Path are required.")
            elif source == 'github' and not repo_url:
                st.error("Repo URL is required for GitHub source.")
            else:
                try:
                    module_config = json.loads(config_json)
                    new_module = {
                        "name": module_name,
                        "module": module_path,
                        "source": source,
                        "repo_url": repo_url if source == 'github' else "",
                        "config": module_config
                    }
                    modules.append(new_module)
                    config['modules'] = modules
                    if save_config(config):
                        st.success(f"Module '{module_name}' added successfully.")
                        logger.info(f"Added new module: {module_name}")
                        # Refresh UI to reflect updated module list
                        st.experimental_rerun()
                    else:
                        st.error("Failed to save configuration. Please check the logs.")
                except json.JSONDecodeError:
                    st.error("Invalid JSON format for configuration.")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    logger.error(f"Error while adding module: {str(e)}")

    # Section to remove an existing module (only show if modules exist)
    if modules:
        st.markdown("### Remove Existing Module")
        with st.form("remove_module_form"):
            module_to_remove = st.selectbox("Select Module to Remove", [module['name'] for module in modules])
            remove_submit = st.form_submit_button("Remove Module")
            if remove_submit:
                modules = [module for module in modules if module['name'] != module_to_remove]
                config['modules'] = modules
                if save_config(config):
                    st.success(f"Module '{module_to_remove}' removed successfully.")
                    logger.info(f"Removed module: {module_to_remove}")
                    # Refresh UI to reflect updated module list
                    st.experimental_rerun()
                else:
                    st.error("Failed to save configuration. Please check the logs.")
    else:
        st.info("No modules to remove.")
