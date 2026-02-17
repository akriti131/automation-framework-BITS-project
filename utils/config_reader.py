import yaml
import os

class ConfigReader:
    def __init__(self):
        config_path = os.path.join("config", "config.yaml")

        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

    def get_browser(self):
        return self.config["browser"]

    def get_base_url(self):
        return self.config["base_url"]

    def get_implicit_wait(self):
        return self.config["implicit_wait"]

    def get_username(self):
        return self.config["credentials"]["username"]

    def get_password(self):
        return self.config["credentials"]["password"]
