import streamlit as st
from utils.config_handler import load_config, save_config
import json
import logging

logger = logging.getLogger(__name__)

def manage_services():
    st.header("🔧 Manage Services")

    # Load current configuration
    config = load_config()

    services = config.get('services', [])

    # Display existing services
    if services:
        st.subheader("Existing Services")
        for service in services:
            st.write(f"**Name:** {service.get('name')}")
            st.write(f"**Type:** {service.get('type')}")
            st.write(f"**Configuration:** {json.dumps(service.get('config', {}), indent=2)}")
            st.write("---")
    else:
        st.info("No services configured yet.")

    # Section to add a new service
    st.markdown("### Add New Service")
    with st.form("add_service_form"):
        service_name = st.text_input("Service Name", "")
        service_type = st.selectbox("Service Type", ["API", "Database", "Other"])
        config_json = st.text_area("Configuration (JSON)", "{}")
        submit = st.form_submit_button("Add Service")

        if submit:
            if not service_name or not service_type:
                st.error("Service Name and Service Type are required.")
            else:
                try:
                    service_config = json.loads(config_json)
                    new_service = {
                        "name": service_name,
                        "type": service_type,
                        "config": service_config
                    }
                    services.append(new_service)
                    config['services'] = services
                    if save_config(config):
                        st.success(f"Service '{service_name}' added successfully.")
                        logger.info(f"Added new service: {service_name}")
                        # Refresh UI to reflect updated service list
                        st.experimental_rerun()
                    else:
                        st.error("Failed to save configuration. Please check the logs.")
                except json.JSONDecodeError:
                    st.error("Invalid JSON format for configuration.")
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")
                    logger.error(f"Error while adding service: {str(e)}")

    # Section to remove an existing service (only show if services exist)
    if services:
        st.markdown("### Remove Existing Service")
        with st.form("remove_service_form"):
            service_to_remove = st.selectbox("Select Service to Remove", [service['name'] for service in services])
            remove_submit = st.form_submit_button("Remove Service")
            if remove_submit:
                services = [service for service in services if service['name'] != service_to_remove]
                config['services'] = services
                if save_config(config):
                    st.success(f"Service '{service_to_remove}' removed successfully.")
                    logger.info(f"Removed service: {service_to_remove}")
                    # Refresh UI to reflect updated service list
                    st.experimental_rerun()
                else:
                    st.error("Failed to save configuration. Please check the logs.")
    else:
        st.info("No services to remove.")
