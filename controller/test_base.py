"""
"""
import logging
import os
import unittest

import util.config_reader as cf
import logger.custom_logger as cl
from util.excel_handler import ExcelHandler
from util.event_handler import EventHandler


class TestBase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.log = cl.custom_logger(logging.DEBUG)
        self.config = cf.read_config_file()
        self.current_folder_path = os.path.split(os.getcwd())
        self.excel_handler = ExcelHandler()
        self.event_handler = EventHandler()












