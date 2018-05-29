"""
Base class

"""
import logging
import os
import unittest

import util.config_reader as cf
import logger.custom_logger as cl
from util.excel_handler import ExcelHandler
from util.event_handler import EventHandler


class TestBase(unittest.TestCase):
    log = cl.custom_logger(logging.DEBUG)
    config = cf.read_config_file()
    current_folder_path = os.path.split(os.getcwd())
    excel_handler = ExcelHandler()
    event_handler = EventHandler()

    def __init__(self, *args, **kwargs):
          unittest.TestCase.__init__(self, *args, **kwargs)












