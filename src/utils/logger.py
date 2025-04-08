import json
import logging
import logging.config
import os
from pathlib import Path


def setup_logging(env_key="LOG_CFG", config_path=None, log_dir=None, env=None):
    """
    Setup logging configuration based on environment

    Args:
        env_key: Environment variable that can be used to override config path
        config_path: Path to the logging config file
        log_dir: Directory where logs will be stored
        env: Environment name (development, testing, staging, production)
              If None, will be determined from APP_ENV environment variable
    """
    # Create logs directory if it doesn't exist
    if log_dir is None:
        log_dir = Path(__file__).parents[2] / "logs"
    Path(log_dir).mkdir(exist_ok=True)

    # Get environment from environment variable if not provided
    if env is None:
        env = os.environ.get("APP_ENV", "development").lower()

    # Default log levels by environment
    env_levels = {
        "development": logging.DEBUG,
        "testing": logging.INFO,
        "staging": logging.INFO,
        "production": logging.WARNING,
    }

    # Get config path from environment variable or use default
    if config_path is None:
        config_path = os.getenv(
            env_key, str(Path(__file__).parents[2] / "config" / "logging.json")
        )

    if os.path.exists(config_path):
        with open(config_path, "rt") as f:
            try:
                config = json.load(f)

                # Set root logger level based on environment if not explicitly defined
                if env in env_levels:
                    if "root" in config and "level" not in config["root"]:
                        config["root"]["level"] = logging.getLevelName(env_levels[env])

                # Replace placeholders with actual values
                for handler in config.get("handlers", {}).values():
                    if "filename" in handler:
                        # Replace the placeholder with the actual log directory
                        handler["filename"] = os.path.join(
                            log_dir, os.path.basename(handler["filename"])
                        )

                logging.config.dictConfig(config)
                logger = logging.getLogger(__name__)
                logger.info(f"Logging configured for environment: {env.upper()}")
                logger.info(f"Log files will be stored in {log_dir}")
            except Exception as e:
                print(f"Error loading logging configuration: {e}")
                default_level = env_levels.get(env, logging.INFO)
                logging.basicConfig(level=default_level)
                print(
                    f"Using basic configuration at level {logging.getLevelName(default_level)}"
                )
    else:
        default_level = env_levels.get(env, logging.INFO)
        logging.basicConfig(level=default_level)
        print(
            f"Config file not found at {config_path}. Using basic configuration at level {logging.getLevelName(default_level)}"
        )


def get_logger(name):
    """Get a logger with the specified name"""
    return logging.getLogger(name)


# Initialize logging when the module is imported
setup_logging()
