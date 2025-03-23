import json
import logging.config

# Load the JSON configuration into a Python dictionary.
config = json.loads("config/logging.json")

# Configure logging using the dictionary configuration.
logging.config.dictConfig(config)
