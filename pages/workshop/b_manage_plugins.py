import streamlit as st
from utils.config_handler import load_config, save_config
import json
import logging

logger = logging.getLogger(__name__)

def manage_plugins():
    st.header("🔌 Manage Plugins")

    # Load current configuration
    config = load_config()

    plugins = config.get('plugins', [])

    # Display existing plugins
    if plugins:
        st.subheader("Existing Plugins")
        for plugin in plugins:
            st.write(f"**Name:** {plugin.get('name')}")
            st.write(f"**Module:** {plugin.get('module')}")
            st.write(f"**Source:** {plugin.get('source', 'local')}")
            if plugin.get('source') == 'github':
                st.write(f"**Repo URL:** {plugin.get('repo_url')}")
            st.write("---")
    else:
        st.info("No plugins configured yet.")

    # Section to add a new plugin
    st.markdown("### Add New Plugin")
    with st.form("add_plugin_form"):
        plugin_name = st.text_input("Plugin Name", "")
        module_name = st.text_input("Module Name", "")
        source = st.selectbox("Source", ["local", "github"])
        repo_url = st.text_input("GitHub Repo URL (if applicable)", "")
        config_json = st.text_area("Configuration (JSON)", "{}")
        submit = st.form_submit_button("Add Plugin")

        if submit:
            if not plugin_name or not module_name:
                st.error("Plugin Name and Module Name are required.")
            elif source == 'github' and not repo_url:
                st.error("Repo URL is required for GitHub source.")
            else:
                try:
                    plugin_config = json.loads(config_json)
                    new_plugin = {
                        "name": plugin_name,
                        "module": module_name,
                        "source": source,
                        "repo_url": repo_url if source == 'github' else "",
                        "config": plugin_config
                    }
                    plugins.append(new_plugin)
                    config['plugins'] = plugins
                    if save_config(config):
                        st.success(f"Plugin '{plugin_name}' added successfully.")
                        logger.info(f"Added new plugin: {plugin_name}")
                        # Refresh UI to show updated plugin list
                        st.experimental_rerun()
                    else:
                        st.error("Failed to save configuration. Please check the logs.")
                except json.JSONDecodeError:
                    st.error("Invalid JSON format for configuration.")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    logger.error(f"Error while adding plugin: {str(e)}")

    # Section to remove an existing plugin (only show if plugins exist)
    if plugins:
        st.markdown("### Remove Existing Plugin")
        with st.form("remove_plugin_form"):
            plugin_to_remove = st.selectbox("Select Plugin to Remove", [plugin['name'] for plugin in plugins])
            remove_submit = st.form_submit_button("Remove Plugin")
            if remove_submit:
                plugins = [plugin for plugin in plugins if plugin['name'] != plugin_to_remove]
                config['plugins'] = plugins
                if save_config(config):
                    st.success(f"Plugin '{plugin_to_remove}' removed successfully.")
                    logger.info(f"Removed plugin: {plugin_to_remove}")
                    # Refresh UI to reflect updated plugin list
                    st.experimental_rerun()
                else:
                    st.error("Failed to save configuration. Please check the logs.")
    else:
        st.info("No plugins to remove.")
