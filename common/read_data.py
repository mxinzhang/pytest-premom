import yaml
import json
from configparser import ConfigParser
from common.logger import logger


class MyConfigParser(ConfigParser):
    """
    Custom ConfigParser class that overrides the optionxform function to prevent the conversion of option keys to lowercase.
    """

    def __init__(self, defaults=None):
        """
        Initializes the MyConfigParser object.
        """
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        """
        Overrides the optionxform function to prevent the conversion of option keys to lowercase.
        """
        return optionstr


class ReadFileData:
    """
    Class for reading data from different file types.
    """

    def __init__(self):
        """
        Initializes the ReadFileData object.
        """
        pass

    def load_yaml(self, file_path):
        """
        Loads data from a YAML file.

        Args:
            file_path (str): The path to the YAML file.

        Returns:
            dict: The data loaded from the YAML file.
        """
        logger.info("Loading {} file...".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        logger.info("Data loaded: {}".format(data))
        return data

    def load_json(self, file_path):
        """
        Loads data from a JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: The data loaded from the JSON file.
        """
        logger.info("Loading {} file...".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        logger.info("Data loaded: {}".format(data))
        return data

    def load_ini(self, file_path):
        """
        Loads data from an INI file.

        Args:
            file_path (str): The path to the INI file.

        Returns:
            dict: The data loaded from the INI file.
        """
        logger.info("Loading {} file...".format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        return data


data = ReadFileData()
