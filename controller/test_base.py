"""
"""
import logging
import os
import unittest

import util.config_reader as cf
import logger.custom_logger as cl
from util.excel_handler import ExcelHandle
from util.test_util import TestUtil


class TestBase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)
        self.log = cl.custom_logger(logging.DEBUG)
        self.config = cf.read_config_file()
        self.current_folder_path = os.path.split(os.getcwd())
        self.excel_handler = ExcelHandle()
        self.utility = TestUtil()

    def setUp(self):
        self.sheet_name = self.excel_handler.open_excel_file(self.current_folder_path[0] +
                                           self.config.get('FileSection', 'ExcelSheetLocation').replace("'", "")
                                           , self.config.get('WorkSheet', 'SanitySheet').replace("'", ""))[0]









