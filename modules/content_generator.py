
# modules/content_generator.py

import logging
from typing import List

logger = logging.getLogger(__name__)

def generate_content(agent, plugin, tools, input_data, options):
    try:
        response = plugin.execute(agent, tools, input_data, options, stream=options.get("stream", False))
        logger.info(f"Generated content with prompt: {input_data.get("prompt", "")}")
        return response
    except Exception as e:
        logger.error(f"Error generating content: {e}")
        raise e
