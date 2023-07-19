import yaml
import json
from configparser import ConfigParser
from common.logger import logger


class MyConfigParser(ConfigParser):
    """
    Custom ConfigParser class that overrides the optionxform function
    to prevent converting option keys to lowercase in .ini files.
    """

    def __init__(self, defaults=None):
        """
        Initialize the MyConfigParser class.

        Args:
            defaults (Optional[dict]): Default values for the parser.
        """
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        """
        Override the optionxform function to return the option key as is.

        Args:
            optionstr (str): The option key.

        Returns:
            str: The option key.
        """
        return optionstr


class ReadFileData():
    """
    Class for reading data from different file formats.
    """

    def __init__(self):
        """
        Initialize the ReadFileData class.
        """
        pass

    def load_yaml(self, file_path):
        """
        Load data from a YAML file.

        Args:
            file_path (str): The path to the YAML file.

        Returns:
            dict: The loaded data.
        """
        logger.info("Loading {} file...".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        logger.info("Data loaded: {}".format(data))
        return data

    def load_json(self, file_path):
        """
        Load data from a JSON file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            dict: The loaded data.
        """
        logger.info("Loading {} file...".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        logger.info("Data loaded: {}".format(data))
        return data

    def load_ini(self, file_path):
        """
        Load data from an INI file.

        Args:
            file_path (str): The path to the INI file.

        Returns:
            dict: The loaded data.
        """
        logger.info("Loading {} file...".format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        return data


data = ReadFileData()
