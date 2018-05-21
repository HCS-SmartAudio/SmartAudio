"""
For custom logs
"""

import inspect
import logging
import os


def custom_logger(loglevel):
    """
    Function for custom logger

    :param loglevel:
    :return: logger object
    """
    current_folder_path = os.path.split(os.getcwd())
    # Gets the name of the class / method from where this method is called
    logger_name = inspect.stack()[1][3]
    logger = logging.getLogger( __name__ )

    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(current_folder_path[0] + '\logs\logs.log'.format(logger_name), mode='w')
    file_handler.setLevel(loglevel)

    formatter = logging.Formatter('%(asctime)s - [%(filename)s: %(funcName)s: %(lineno)d] - %(levelname)s: %(message)s',
                                           datefmt='%d/%m/%Y %I:%M:%S %p')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
