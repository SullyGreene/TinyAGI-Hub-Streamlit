import streamlit as st
from utils.config_handler import load_config, save_config
import json
import logging

logger = logging.getLogger(__name__)

def manage_tools():
    st.header("🛠️ Manage Tools")

    # Load current configuration
    config = load_config()

    tools = config.get('tools', [])

    # Display existing tools
    if tools:
        st.subheader("Existing Tools")
        for tool in tools:
            st.write(f"**Name:** {tool.get('name')}")
            st.write(f"**Module:** {tool.get('module')}")
            st.write(f"**Class:** {tool.get('class', tool.get('name'))}")
            st.write(f"**Source:** {tool.get('source', 'local')}")
            if tool.get('source') == 'github':
                st.write(f"**Repo URL:** {tool.get('repo_url')}")
            st.write("---")
    else:
        st.info("No tools configured yet.")

    # Section to add a new tool
    st.markdown("### Add New Tool")
    with st.form("add_tool_form"):
        tool_name = st.text_input("Tool Name", "")
        module_name = st.text_input("Module Name", "")
        class_name = st.text_input("Class Name (optional)", "")
        source = st.selectbox("Source", ["local", "github"])
        repo_url = st.text_input("GitHub Repo URL (if applicable)", "")
        config_json = st.text_area("Configuration (JSON)", "{}")
        submit = st.form_submit_button("Add Tool")

        if submit:
            if not tool_name or not module_name:
                st.error("Tool Name and Module Name are required.")
            elif source == 'github' and not repo_url:
                st.error("Repo URL is required for GitHub source.")
            else:
                try:
                    tool_config = json.loads(config_json)
                    new_tool = {
                        "name": tool_name,
                        "module": module_name,
                        "class": class_name if class_name else tool_name,
                        "source": source,
                        "repo_url": repo_url if source == 'github' else "",
                        "config": tool_config
                    }
                    tools.append(new_tool)
                    config['tools'] = tools
                    if save_config(config):
                        st.success(f"Tool '{tool_name}' added successfully.")
                        logger.info(f"Added new tool: {tool_name}")
                        # Refresh UI to reflect updated tool list
                        st.experimental_rerun()
                    else:
                        st.error("Failed to save configuration. Please check the logs.")
                except json.JSONDecodeError:
                    st.error("Invalid JSON format for configuration.")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    logger.error(f"Error while adding tool: {str(e)}")

    # Section to remove an existing tool (only show if tools exist)
    if tools:
        st.markdown("### Remove Existing Tool")
        with st.form("remove_tool_form"):
            tool_to_remove = st.selectbox("Select Tool to Remove", [tool['name'] for tool in tools])
            remove_submit = st.form_submit_button("Remove Tool")
            if remove_submit:
                tools = [tool for tool in tools if tool['name'] != tool_to_remove]
                config['tools'] = tools
                if save_config(config):
                    st.success(f"Tool '{tool_to_remove}' removed successfully.")
                    logger.info(f"Removed tool: {tool_to_remove}")
                    # Refresh UI to reflect updated tool list
                    st.experimental_rerun()
                else:
                    st.error("Failed to save configuration. Please check the logs.")
    else:
        st.info("No tools to remove.")
