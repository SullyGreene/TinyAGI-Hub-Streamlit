import streamlit as st
from dotenv import load_dotenv
import os
import logging

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(
    level=os.getenv('LOG_LEVEL', 'INFO').upper(),
    format='%(asctime)s %(levelname)s:%(name)s:%(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

# Clone or update the TinyAGI-Hub repository
from utils.git_manager import clone_or_update_repo

HUB_REPO_URL = "https://github.com/SullyGreene/TinyAGI-Hub.git"
HUB_REPO_DIR = "TinyAGI-Hub"

clone_or_update_repo(HUB_REPO_URL, HUB_REPO_DIR)

# Streamlit App Configuration
st.set_page_config(page_title="TinyAGI Hub", layout="wide")

# Title
st.title("🤖 TinyAGI Hub")

# Sidebar Navigation
st.sidebar.title("Navigation")

# Callback functions to handle selection changes
def on_manage_selection_change():
    st.session_state['page'] = st.session_state['manage_selection']
    st.session_state['other_selection'] = None

def on_other_selection_change():
    st.session_state['page'] = st.session_state['other_selection']
    st.session_state['manage_selection'] = None

# Initialize session state variables
if 'page' not in st.session_state:
    st.session_state['page'] = 'Dashboard'  # Default page
    st.session_state['manage_selection'] = None
    st.session_state['other_selection'] = 'Dashboard'

with st.sidebar.expander("🔧 Manage Components", expanded=True):
    manage_pages = [
        "Manage Agents",
        "Manage Plugins",
        "Manage Tools",
        "Manage Modules",
        "Manage Services"
    ]
    st.radio(
        "Manage Components",
        options=manage_pages,
        key='manage_selection',
        on_change=on_manage_selection_change
    )

with st.sidebar.expander("⚙️ Configurations & Execution", expanded=False):
    other_pages = [
        "Dashboard",
        "Configuration Builder",
        "Task Execution",
        "Hub Integration"
    ]
    st.radio(
        "App Sections",
        options=other_pages,
        key='other_selection',
        on_change=on_other_selection_change
    )

# Get the current page from session state
page = st.session_state['page']

# Display breadcrumb-like navigation at the top of the page
st.markdown(f"### You are here: {page}")

# Display the page's content
if page == "Dashboard":
    st.subheader("📊 Dashboard")
    st.write("Welcome to TinyAGI Hub! Use the sidebar to navigate through the different sections.")
    st.image(
        "https://raw.githubusercontent.com/SullyGreene/TinyAGI-Hub/main/images/tinyagi_logo.png",
        width=300
    )
    st.info("This page provides an overview of TinyAGI Hub, including system information and recent activity.")

elif page == "Manage Agents":
    st.subheader("🔧 Manage Agents")
    st.info("On this page, you can add, remove, or modify agents in your TinyAGI system.")
    from pages.workshop.a_manage_agents import manage_agents
    manage_agents()

elif page == "Manage Plugins":
    st.subheader("🔌 Manage Plugins")
    st.info("Plugins extend the capabilities of TinyAGI. Here, you can manage the plugins, add new ones, or remove existing ones.")
    from pages.workshop.b_manage_plugins import manage_plugins
    manage_plugins()

elif page == "Manage Tools":
    st.subheader("🛠 Manage Tools")
    st.info("Tools are external utilities that TinyAGI uses. This page allows you to add, configure, or remove tools.")
    from pages.workshop.c_manage_tools import manage_tools
    manage_tools()

elif page == "Manage Modules":
    st.subheader("📦 Manage Modules")
    st.info("Modules are additional capabilities you can add to TinyAGI. Manage and configure them here.")
    from pages.workshop.d_manage_modules import manage_modules
    manage_modules()

elif page == "Manage Services":
    st.subheader("⚙️ Manage Services")
    st.info("Manage background services used by TinyAGI on this page. Start, stop, or configure services as needed.")
    from pages.workshop.e_manage_services import manage_services
    manage_services()

elif page == "Configuration Builder":
    st.subheader("🛠️ Configuration Builder")
    st.info("Use this page to create or modify configuration files that TinyAGI uses to control its behavior.")
    from pages.workshop.f_configuration_builder import configuration_builder
    configuration_builder()

elif page == "Task Execution":
    st.subheader("🚀 Task Execution")
    st.info("Execute predefined tasks configured in TinyAGI. You can select a task and initiate its execution here.")
    from pages.workshop.g_task_execution import task_execution
    task_execution()

elif page == "Hub Integration":
    st.subheader("🔗 Hub Integration")
    st.info("Explore the TinyAGI Hub to discover new agents, plugins, modules, and tools contributed by the community.")
    from pages.workshop.h_hub_integration import hub_integration
    hub_integration()
