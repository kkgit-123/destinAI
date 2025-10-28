import configparser
import os

class ConfigReader:
    """
    A utility class to read configuration from a config.ini file.
    """
    def __init__(self, config_file=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), 'config.ini')):
        """
        Initializes the ConfigReader with the path to the configuration file.

        Args:
            config_file (str): The path to the config.ini file. Defaults to 'config.ini'
                               located in the parent 'api_server' directory. This path can be
                               absolute or relative to the current working directory of the
                               script that instantiates ConfigReader.
        """
        self.config = configparser.ConfigParser()
        self.config_file = config_file
        self._load_config()

    def _load_config(self):
        """Loads the configuration from the specified file."""
        if not os.path.exists(self.config_file):
            raise FileNotFoundError(f"Config file not found: {self.config_file}")
        self.config.read(self.config_file)

    def get(self, section, option, default=None):
        """
        Retrieves a configuration value.

        Args:
            section (str): The section name in the config file.
            option (str): The option name within the section.
            default (any, optional): Default value to return if the option is not found.

        Returns:
            str: The configuration value.
        """
        try:
            return self.config.get(section, option)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return default

    def get_image_base_path(self):
        """
        Retrieves the image base path.
        """
        return self.get('paths', 'image_base_path', 'destinAI/api_server/files/images')

    def getboolean(self, section, option, default=None):
        """
        Retrieves a boolean configuration value.
        """
        try:
            return self.config.getboolean(section, option)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return default

    def getint(self, section, option, default=None):
        """
        Retrieves an integer configuration value.
        """
        try:
            return self.config.getint(section, option)
        except (configparser.NoSectionError, configparser.NoOptionError):
            return default
