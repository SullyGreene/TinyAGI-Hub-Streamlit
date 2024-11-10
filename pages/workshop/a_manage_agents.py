import streamlit as st
from utils.config_handler import load_config, save_config
import json
import logging

logger = logging.getLogger(__name__)

def manage_agents():
    st.header("🧠 Manage Agents")

    # Load current configuration
    config = load_config()

    agents = config.get('agents', [])

    # Display existing agents
    if agents:
        st.subheader("Existing Agents")
        for agent in agents:
            st.write(f"**Name:** {agent.get('name')}")
            st.write(f"**Module:** {agent.get('module')}")
            st.write(f"**Class:** {agent.get('class', agent.get('name'))}")
            st.write("---")
    else:
        st.info("No agents configured yet.")

    # Section to add a new agent
    st.markdown("### Add New Agent")
    with st.form("add_agent_form"):
        agent_name = st.text_input("Agent Name", "")
        module_name = st.text_input("Module Name", "")
        class_name = st.text_input("Class Name (optional)", "")
        config_json = st.text_area("Configuration (JSON)", "{}")
        submit = st.form_submit_button("Add Agent")

        if submit:
            if not agent_name or not module_name:
                st.error("Agent Name and Module Name are required.")
            else:
                try:
                    agent_config = json.loads(config_json)
                    new_agent = {
                        "name": agent_name,
                        "module": module_name,
                        "class": class_name if class_name else agent_name,
                        "config": agent_config
                    }
                    agents.append(new_agent)
                    config['agents'] = agents
                    if save_config(config):
                        st.success(f"Agent '{agent_name}' added successfully.")
                        logger.info(f"Added new agent: {agent_name}")
                        # Rerun the script to update the UI with the new agent
                        st.experimental_rerun()
                    else:
                        st.error("Failed to save configuration. Please check the logs.")
                except json.JSONDecodeError:
                    st.error("Invalid JSON format for configuration.")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    logger.error(f"Error while adding agent: {str(e)}")

    # Section to remove an existing agent (only show if agents exist)
    if agents:
        st.markdown("### Remove Existing Agent")
        with st.form("remove_agent_form"):
            agent_to_remove = st.selectbox("Select Agent to Remove", [agent['name'] for agent in agents])
            remove_submit = st.form_submit_button("Remove Agent")
            if remove_submit:
                agents = [agent for agent in agents if agent['name'] != agent_to_remove]
                config['agents'] = agents
                if save_config(config):
                    st.success(f"Agent '{agent_to_remove}' removed successfully.")
                    logger.info(f"Removed agent: {agent_to_remove}")
                    # Rerun the script to update the UI after removing the agent
                    st.experimental_rerun()
                else:
                    st.error("Failed to save configuration. Please check the logs.")
    else:
        st.info("No agents to remove.")
