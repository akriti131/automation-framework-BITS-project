import yaml
import os


class DataReader:

    @staticmethod
    def load_yaml(file_name):
        file_path = os.path.join("test_data", file_name)

        with open(file_path, "r") as file:
            return yaml.safe_load(file)