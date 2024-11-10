
# modules/emojifier.py

import emoji
from modules.config_manager import load_config

def emojify_text(text):
    config = load_config()
    if config.get('EMOJIAI'):
        return emoji.emojize(text, language='alias')
    else:
        return text
