"""

Reads data from config file

"""

import ConfigParser
import os


def read_config_file():
    """
    :return: config data

    """
    config = ConfigParser.ConfigParser()
    current_folder_path = os.path.split(os.getcwd())
    config.read(current_folder_path[0] + "\properties\config.properties")

    return config
