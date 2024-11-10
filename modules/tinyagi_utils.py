
# modules/tinyagi_utils.py

import streamlit as st
from TinyAGI import AgentSystem
import os
import logging
from logging.handlers import RotatingFileHandler
from modules.config_manager import load_config, save_config
from modules.emojifier import emojify_text

# Set up logging with rotating file handler
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
handler = RotatingFileHandler("tinyagi_streamlit.log", maxBytes=5000000, backupCount=5)
logger.addHandler(handler)

# Directory containing configuration files for TinyAGI
CONFIG_DIR = "config/content_creator"
# List all JSON configuration files in the directory
config_files = [f"{CONFIG_DIR}/{file}" for file in os.listdir(CONFIG_DIR) if file.endswith(".json")]

def load_agent_system():
    if not config_files:
        st.sidebar.error(emojify_text("No configuration files found in the 'config/content_creator' directory."))
        st.sidebar.text(emojify_text("Please add a configuration file to proceed."))
        st.stop()

    # Allow the user to select a configuration file from the available options
    config_file_path = st.sidebar.selectbox(emojify_text("Select Configuration File"), config_files)

    if not os.path.exists(config_file_path):
        st.error(emojify_text(f"Configuration file '{config_file_path}' not found."))
        st.stop()

    agent_system = AgentSystem(config_files=config_file_path)
    logger.info(f"AgentSystem loaded with configuration: {config_file_path}")
    return agent_system

def setup_tinyagi():
    st.sidebar.header(emojify_text("TinyAGI Configuration"))
    agent_system = load_agent_system()

    # Initialize plugin, tool, and agent managers
    plugin_manager = agent_system.plugin_manager
    tool_manager = agent_system.tool_manager
    agent_manager = agent_system.agent_manager

    # List available agents and allow the user to select one
    agent_names = list(agent_manager.loaded_agents.keys())
    selected_agent = st.sidebar.selectbox(emojify_text("Select an Agent"), agent_names)

    # List available plugins and allow the user to select one
    plugin_names = list(plugin_manager.loaded_plugins.keys())
    selected_plugin = st.sidebar.selectbox(emojify_text("Select a Plugin"), plugin_names)

    # List available tools and allow the user to select multiple tools
    tool_names = list(tool_manager.loaded_tools.keys())
    selected_tools = st.sidebar.multiselect(emojify_text("Select Tools"), tool_names)

    # Retrieve the selected agent, plugin, and tools
    agent = agent_manager.get_agent(selected_agent)
    plugin = plugin_manager.get_plugin(selected_plugin)
    tools = [tool_manager.get_tool(tool_name) for tool_name in selected_tools]

    # EMOJIAI Toggle
    config = load_config()
    emojiai_state = st.sidebar.checkbox(emojify_text("Enable EMOJIAI"), value=config.get("EMOJIAI", False))
    if emojiai_state != config.get("EMOJIAI", False):
        config["EMOJIAI"] = emojiai_state
        save_config(config)
        st.rerun()

    # If you need user info, access it without parentheses
    # user_info = st.experimental_user

    return agent_system, agent, plugin, tools

def display_configuration(agent_system):
    with st.sidebar:
        st.header(emojify_text("Loaded Configuration"))
        if st.checkbox(emojify_text("Show Configuration")):
            st.json(agent_system.config)
