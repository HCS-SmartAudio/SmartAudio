"""
"""
import logging

import util.config_reader as cf
import logger.custom_logger as cl


class TestBase(object):
    def __init__(self):
        self.log = cl.custom_logger(logging.DEBUG)
        self.config = cf.read_config_file()




