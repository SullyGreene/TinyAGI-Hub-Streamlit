
import json
import os
import logging

logger = logging.getLogger(__name__)

def load_config(config_path='agent_config.json'):
    if not os.path.exists(config_path):
        logger.warning(f"Config file '{config_path}' not found. Returning empty config.")
        return {}
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = json.load(f)
        logger.info(f"Loaded configuration from '{config_path}'.")
        return config
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error in config file '{config_path}': {e}")
        return {}
    except Exception as e:
        logger.error(f"Error loading config file '{config_path}': {e}")
        return {}

def save_config(config, config_path='agent_config.json'):
    try:
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)
        logger.info(f"Configuration saved to '{config_path}'.")
    except Exception as e:
        logger.error(f"Error saving config file '{config_path}': {e}")
