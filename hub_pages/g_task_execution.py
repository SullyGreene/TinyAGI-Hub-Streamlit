import streamlit as st
from utils.config_handler import load_config, save_config
import json
import logging

logger = logging.getLogger(__name__)

def task_execution():
    st.header("📋 Task Execution")

    # Load current configuration
    config = load_config()

    tasks = config.get('tasks', [])

    # Display existing tasks
    if tasks:
        st.subheader("Existing Tasks")
        for task in tasks:
            st.write(f"**Task ID:** {task.get('task_id')}")
            st.write(f"**Plugin:** {task.get('plugin')}")
            st.write(f"**Agent:** {task.get('agent')}")
            st.write(f"**Tool:** {task.get('tool', 'None')}")
            st.write(f"**Input:** {json.dumps(task.get('input', {}), indent=2)}")
            st.write(f"**Options:** {json.dumps(task.get('options', {}), indent=2)}")
            st.write("---")
    else:
        st.info("No tasks configured yet.")

    # Add new task form
    st.markdown("### Add New Task")
    with st.form("add_task_form"):
        task_id = st.text_input("Task ID", "")
        plugin = st.text_input("Plugin Name", "")
        agent = st.text_input("Agent Name", "")
        tool = st.text_input("Tool Name (optional)", "")
        input_json = st.text_area("Input Data (JSON)", "{}")
        options_json = st.text_area("Options (JSON)", "{}")
        submit = st.form_submit_button("Add Task")

        if submit:
            if not task_id or not plugin or not agent:
                st.error("Task ID, Plugin Name, and Agent Name are required.")
            else:
                try:
                    input_data = json.loads(input_json)
                    options = json.loads(options_json)
                    new_task = {
                        "task_id": task_id,
                        "plugin": plugin,
                        "agent": agent,
                        "tool": tool if tool else "",
                        "input": input_data,
                        "options": options
                    }
                    tasks.append(new_task)
                    config['tasks'] = tasks
                    if save_config(config):
                        st.success(f"Task '{task_id}' added successfully.")
                        logger.info(f"Added new task: {task_id}")
                        # Refresh UI to reflect updated tasks list
                        st.experimental_rerun()
                    else:
                        st.error("Failed to save configuration. Please check the logs.")
                except json.JSONDecodeError:
                    st.error("Invalid JSON format for Input Data or Options.")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    logger.error(f"Error while adding task: {str(e)}")

    # Remove existing task form (only show if tasks exist)
    if tasks:
        st.markdown("### Remove Existing Task")
        with st.form("remove_task_form"):
            task_to_remove = st.selectbox("Select Task to Remove", [task['task_id'] for task in tasks])
            remove_submit = st.form_submit_button("Remove Task")
            if remove_submit:
                tasks = [task for task in tasks if task['task_id'] != task_to_remove]
                config['tasks'] = tasks
                if save_config(config):
                    st.success(f"Task '{task_to_remove}' removed successfully.")
                    logger.info(f"Removed task: {task_to_remove}")
                    # Refresh UI to reflect updated tasks list
                    st.experimental_rerun()
                else:
                    st.error("Failed to save configuration. Please check the logs.")
    else:
        st.info("No tasks to remove.")

    # Execute task section
    if tasks:
        st.markdown("### Execute Task")
        selected_task_id = st.selectbox("Select Task to Execute", [task['task_id'] for task in tasks])
        if st.button("Execute Task"):
            task = next((t for t in tasks if t['task_id'] == selected_task_id), None)
            if task:
                with st.spinner(f"Executing Task '{selected_task_id}'..."):
                    try:
                        # Initialize AgentSystem with current config
                        from TinyAGI import AgentSystem
                        agent_system = AgentSystem(config_files=['agent_config.json'])
                        agent_manager = agent_system.agent_manager
                        plugin_manager = agent_system.plugin_manager
                        tool_manager = agent_system.tool_manager
                        task_manager = agent_system.task_manager

                        # Get components
                        plugin = plugin_manager.get_plugin(task['plugin'])
                        agent = agent_manager.get_agent(task['agent'])
                        tool = tool_manager.get_tool(task['tool']) if task['tool'] else None

                        if not plugin:
                            st.error(f"Plugin '{task['plugin']}' not found.")
                            return
                        if not agent:
                            st.error(f"Agent '{task['agent']}' not found.")
                            return

                        # Execute the task
                        response = plugin.execute(
                            agent=agent,
                            tool=tool,
                            input_data=task.get('input', {}),
                            options=task.get('options', {}),
                            stream=task.get('options', {}).get('stream', False)
                        )

                        st.success(f"Task '{selected_task_id}' executed successfully.")
                        st.write("### Output:")
                        st.write(response)

                    except Exception as e:
                        st.error(f"Error executing task: {e}")
                        logger.error(f"Error executing task '{selected_task_id}': {e}")
            else:
                st.error(f"Task '{selected_task_id}' not found.")
    else:
        st.info("No tasks available to execute.")

