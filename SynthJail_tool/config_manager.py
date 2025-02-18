import configparser
import os
from synthjail.logger import Logger

class ConfigManager:
    def __init__(self):
        self.logger = Logger()
        self.config = configparser.ConfigParser()
        self.config_path = os.path.join(os.path.dirname(__file__), "../config.ini")
        self._load_config()

    def _load_config(self):
        if not os.path.exists(self.config_path):
            self.logger.error("Config file not found. Please create a 'config.ini' file.")
            raise FileNotFoundError("config.ini not found.")
        self.config.read(self.config_path)

    def get_api_key(self, model_name):
        try:
            return self.config.get("API_KEYS", model_name)
        except configparser.NoOptionError:
            self.logger.error(f"API key for '{model_name}' not found in config.ini.")
            return None
