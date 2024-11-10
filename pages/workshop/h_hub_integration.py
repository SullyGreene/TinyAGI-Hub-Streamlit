import streamlit as st
from utils.git_manager import clone_or_update_repo
from utils.config_handler import load_config, save_config
import os
import logging
import json

logger = logging.getLogger(__name__)

def hub_integration():
    st.header("🔗 TinyAGI Hub Integration")

    st.markdown("""
    Explore and integrate new agents, plugins, modules, and tools from the TinyAGI Hub. You can browse available components and import them directly into your configuration.
    """)

    HUB_REPO_URL = "https://github.com/SullyGreene/TinyAGI-Hub.git"
    HUB_REPO_DIR = "TinyAGI-Hub"

    if st.button("Clone/Update TinyAGI Hub Repository"):
        with st.spinner("Cloning/Updating repository..."):
            clone_or_update_repo(HUB_REPO_URL, HUB_REPO_DIR)
            st.success("Repository cloned/updated successfully.")

    if os.path.exists(HUB_REPO_DIR):
        st.subheader("🔍 Available Components in Hub")

        components = {
            "Agents": [],
            "Plugins": [],
            "Tools": [],
            "Modules": [],
            "Services": []
        }

        # Iterate through the hub repository to list components
        for root, dirs, files in os.walk(HUB_REPO_DIR):
            for file in files:
                if file.endswith(".py"):
                    relative_path = os.path.relpath(root, HUB_REPO_DIR)
                    component_type = relative_path.capitalize()
                    if component_type in components:
                        component_name = file[:-3]  # Remove .py extension
                        components[component_type].append(component_name)

        # Display components with nicer formatting
        for comp_type, comp_list in components.items():
            if comp_list:
                st.markdown(f"### {comp_type}")
                st.markdown(f"Here are the available **{comp_type.lower()}** from the TinyAGI Hub:")
                
                for comp in comp_list:
                    st.markdown(f"- **{comp}**")
                
                st.markdown("<hr style='border:1px solid #d3d3d3;'>", unsafe_allow_html=True)
                
    else:
        st.error("TinyAGI Hub repository not found. Please clone it first.")

    st.markdown("### 📥 Import Components from Hub")
    st.markdown("""
    Select a component type and name to import it directly into your TinyAGI configuration.
    """)

    with st.form("import_component_form"):
        component_type = st.selectbox("Select Component Type", ["Agents", "Plugins", "Tools", "Modules", "Services"])
        component_name = st.text_input("Component Name", "")
        import_submit = st.form_submit_button("Import Component")

        if import_submit:
            if not component_type or not component_name:
                st.error("Component Type and Component Name are required.")
            else:
                component_path = os.path.join(HUB_REPO_DIR, component_type.lower(), f"{component_name}.py")
                if os.path.exists(component_path):
                    # Read component configuration if any
                    config_path = os.path.join(HUB_REPO_DIR, component_type.lower(), f"{component_name}_config.json")
                    if os.path.exists(config_path):
                        with open(config_path, 'r', encoding='utf-8') as f:
                            component_config = json.load(f)
                    else:
                        component_config = {}

                    # Load current config
                    config = load_config()

                    # Depending on component type, add to config
                    if component_type == "Agents":
                        agents = config.get('agents', [])
                        new_agent = {
                            "name": component_name,
                            "module": component_name,
                            "class": component_name,
                            "config": component_config
                        }
                        agents.append(new_agent)
                        config['agents'] = agents
                        save_config(config)
                        st.success(f"Agent '{component_name}' imported successfully.")

                    elif component_type == "Plugins":
                        plugins = config.get('plugins', [])
                        new_plugin = {
                            "name": component_name,
                            "module": component_name,
                            "source": "local",
                            "config": component_config
                        }
                        plugins.append(new_plugin)
                        config['plugins'] = plugins
                        save_config(config)
                        st.success(f"Plugin '{component_name}' imported successfully.")

                    elif component_type == "Tools":
                        tools = config.get('tools', [])
                        new_tool = {
                            "name": component_name,
                            "module": component_name,
                            "class": component_name,
                            "source": "local",
                            "config": component_config
                        }
                        tools.append(new_tool)
                        config['tools'] = tools
                        save_config(config)
                        st.success(f"Tool '{component_name}' imported successfully.")

                    elif component_type == "Modules":
                        modules = config.get('modules', [])
                        new_module = {
                            "name": component_name,
                            "module": component_name,
                            "source": "local",
                            "config": component_config
                        }
                        modules.append(new_module)
                        config['modules'] = modules
                        save_config(config)
                        st.success(f"Module '{component_name}' imported successfully.")

                    elif component_type == "Services":
                        services = config.get('services', [])
                        new_service = {
                            "name": component_name,
                            "type": component_config.get('type', 'Other'),
                            "config": component_config
                        }
                        services.append(new_service)
                        config['services'] = services
                        save_config(config)
                        st.success(f"Service '{component_name}' imported successfully.")

                else:
                    st.error(f"Component '{component_name}' not found in the Hub repository.")

