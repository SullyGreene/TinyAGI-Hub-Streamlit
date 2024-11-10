
# modules/config_manager.py

import yaml
import os

CONFIG_FILE = 'config.yaml'

def load_config():
    if not os.path.exists(CONFIG_FILE):
        # Create a default config file if it doesn't exist
        default_config = {'EMOJIAI': False}
        with open(CONFIG_FILE, 'w') as file:
            yaml.dump(default_config, file)
        return default_config
    else:
        with open(CONFIG_FILE, 'r') as file:
            return yaml.safe_load(file)

def save_config(config):
    with open(CONFIG_FILE, 'w') as file:
        yaml.dump(config, file)
