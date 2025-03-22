import json
import logging.config

# Define the JSON configuration for logging.
config_json = """
{
    "version": 1,
    "disable_existing_loggers": false,
    "formatters": {
        "consoleFormatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        },
        "fileFormatter": {
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s"
        }
    },
    "handlers": {
        "consoleHandler": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "consoleFormatter",
            "stream": "ext://sys.stdout"
        },
        "fileHandler": {
            "class": "logging.FileHandler",
            "level": "INFO",
            "formatter": "fileFormatter",
            "filename": "app.log",
            "mode": "a",
            "encoding": "utf-8"
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": ["consoleHandler", "fileHandler"]
    }
}
"""

# Load the JSON configuration into a Python dictionary.
config = json.loads(config_json)

# Configure logging using the dictionary configuration.
logging.config.dictConfig(config)

# Create a logger instance.
logger = logging.getLogger(__name__)
