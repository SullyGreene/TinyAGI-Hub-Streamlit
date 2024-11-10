import streamlit as st
from TinyAGI import AgentSystem, PluginManager, ToolManager, ModuleManager, TaskManager
import json
import os
import logging
from logging.handlers import RotatingFileHandler

# Set up logging with rotating file handler to prevent logs from growing indefinitely
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
handler = RotatingFileHandler("task_responses.log", maxBytes=5000000, backupCount=5)
logger.addHandler(handler)

# Directory containing configuration files
CONFIG_DIR = "config"
# List all JSON configuration files in the directory
config_files = [f"{CONFIG_DIR}/{file}" for file in os.listdir(CONFIG_DIR) if file.endswith('.json')]
if not config_files:
    # Display an error if no configuration files are found
    st.sidebar.error("No configuration files found in the 'config' directory.")
    st.sidebar.text("Please add a configuration file to proceed.")
    st.stop()

# Allow the user to select a configuration file from the available options
CONFIG_FILE_PATH = st.sidebar.selectbox("Select Configuration File", config_files)

def load_agent_system(config_path):
    # Load the agent system from the specified configuration file
    if not os.path.exists(config_path):
        st.error(f"Configuration file '{config_path}' not found.")
        return None
    return AgentSystem(config_files=config_path)

def main():
    # Set up the main UI title
    st.title("TinyAGI - Streamlit UI")
    st.sidebar.header("Configuration")
    config_path = CONFIG_FILE_PATH
    agent_system = load_agent_system(config_path)
    
    # Check if the agent system was loaded successfully
    if agent_system is None:
        st.sidebar.error("Failed to load the configuration. Please select a valid configuration file.")
        return
    
    # Initialize plugin, tool, and agent managers
    plugin_manager = agent_system.plugin_manager
    tool_manager = agent_system.tool_manager
    agent_manager = agent_system.agent_manager

    # List available agents and allow the user to select one
    agent_names = list(agent_manager.loaded_agents.keys())
    selected_agent = st.sidebar.selectbox("Select an Agent", agent_names)

    # List available plugins and allow the user to select one
    plugin_names = list(plugin_manager.loaded_plugins.keys())
    selected_plugin = st.sidebar.selectbox("Select a Plugin", plugin_names)

    # List available tools and allow the user to select one, or choose "None"
    tool_names = list(tool_manager.loaded_tools.keys())
    selected_tool = st.sidebar.selectbox("Select a Tool", ["None"] + tool_names)

    # Load tasks from the configuration, ensuring it's a list
    tasks = agent_system.config.get('tasks', [])
    if not isinstance(tasks, list):
        st.sidebar.error("Tasks configuration is not properly formatted. Please check the configuration file.")
        return

    # List available tasks and allow the user to select one
    task_names = [task.get('task_id', f"Task {i+1}") for i, task in enumerate(tasks)]
    selected_task = st.sidebar.selectbox("Select a Task", ["None"] + task_names)

    # Retrieve the selected agent, plugin, and tool
    agent = agent_manager.get_agent(selected_agent)
    plugin = plugin_manager.get_plugin(selected_plugin)
    tool = None
    if selected_tool != "None":
        tool = tool_manager.get_tool(selected_tool)
    # Retrieve the selected task if one is chosen
    task = tasks[task_names.index(selected_task) - 1] if selected_task != "None" else None

    with st.sidebar.container():
        st.header("Task Execution")
        # Display the prompt for the selected task, or allow the user to enter a custom prompt
        if task:
            prompt = task.get('input', {}).get('prompt', '')
            st.text_area("Task Prompt", prompt, disabled=True)
        else:
            prompt = st.text_area("Prompt for the Agent")
        # Checkbox to allow streaming output
        stream = st.checkbox("Stream Output", value=False)

        # Execute the task when the button is pressed
        if st.button("Execute Task"):
            if not prompt:
                st.error("Please provide a prompt to execute.")
            else:
                with st.spinner("Executing Task..."):
                    try:
                        # Check if the plugin and agent are properly loaded
                        if not plugin or not agent:
                            st.error("Selected plugin or agent is not available. Please verify your selection.")
                            return

                        # Prepare input data and options for execution
                        input_data = {"prompt": prompt}
                        options = {"stream": stream}
                        response = plugin.execute(agent, tool, input_data, options, stream=stream)

                        logger.info(f"Executed task with prompt: {prompt}")

                        # Display the response, handling streaming if enabled
                        if stream:
                            for chunk in response:
                                st.write(chunk)
                        else:
                            st.write(response)

                        # Log the response
                        logger.info(f"Prompt: {prompt}\nResponse: {response}\n{'-' * 80}\n")
                    except ValueError as e:
                        st.error(f"Value error: {str(e)}")
                        logger.error(f"Value error during task execution: {str(e)}")
                    except ConnectionError as e:
                        st.error(f"Network error: {str(e)}. Please check your connection.")
                        logger.error(f"Network error during task execution: {str(e)}")
                    except Exception as e:
                        st.error(f"Unexpected error: {str(e)}")
                        logger.error(f"Unexpected error during task execution: {str(e)}")

    # Chat interface with the agent
    st.header("Chat with Agent")
    chat_prompt = st.chat_input("Your message")
    if chat_prompt:
        with st.spinner("Processing chat input..."):
            try:
                # Check if the plugin and agent are properly loaded
                if not plugin or not agent:
                    st.error("Selected plugin or agent is not available. Please verify your selection.")
                    return

                # Execute the chat prompt using the selected plugin and agent
                input_data = {"prompt": chat_prompt}
                response = plugin.execute(agent, tool, input_data, options={}, stream=False)
                st.write(f"Agent: {response}")

                # Log the chat prompt and response
                logger.info(f"Chat input: {chat_prompt}\nResponse: {response}")
                logger.info(f"Chat Prompt: {chat_prompt}\nChat Response: {response}\n{'-' * 80}\n")
            except ValueError as e:
                st.error(f"Value error: {str(e)}")
                logger.error(f"Value error during chat input: {str(e)}")
            except ConnectionError as e:
                st.error(f"Network error: {str(e)}. Please check your connection.")
                logger.error(f"Network error during chat input: {str(e)}")
            except Exception as e:
                st.error(f"Unexpected error: {str(e)}")
                logger.error(f"Unexpected error during chat input: {str(e)}")

    # Display the loaded configuration in the sidebar
    with st.sidebar:
        st.header("Loaded Configuration")
        if st.checkbox("Show Configuration"):
            st.json(agent_system.config)

if __name__ == "__main__":
    main()
