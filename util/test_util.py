"""
Class for maintaining common test functions
"""
import re
import os
import logging
import xml.etree.cElementTree as ET

import util.config_reader as cf
import logger.custom_logger as cl


class TestUtil():
    """
     Test Utility Class
    """
    search_list = ['power on', 'power off', 'power down']
    current_folder_path = os.path.split(os.getcwd())
    config = cf.read_config_file()
    log = cl.custom_logger(logging.DEBUG)

    def search_for_event_key(self, cell_data):
        """
        Searches event exists from cell
        :param cell_data:
        :return: Event search name
        """
        for element in self.search_list:
            if re.search(element, cell_data.lower()):
                return element
        #return "Key Not Found"

    def search_for_event_id(self, key_name):
       """
       Searches event key id
       :param key_name:
       :return: Event id
       """
       DOMTree = ET.parse(self.current_folder_path[0] +
                          self.config.get('FileSection', 'EventKeyFileLocation').replace("'", ""))
       keys = key_name.split(" ")
       item_list = DOMTree.getroot()

       for elem in item_list.findall("./" + keys[0] + "/" + keys[1]):
            key_id = elem.attrib

       self.log.info("Event id found %s", key_id['id'])

       return key_id['id']

    def search_for_event_value(self, key_name):
        """
        Searches event key value
        param key_name:
        :return: Event value
        """
        DOMTree = ET.parse(self.current_folder_path[0] +
                           self.config.get('FileSection', 'EventKeyFileLocation').replace("'", ""))
        keys = key_name.split(" ")

        item_list = DOMTree.getroot()

        for elem in item_list.findall("./" + keys[0] + "/" + keys[1]):
            key_value = elem.text

        self.log.info("Event id found %s", key_value)

        return key_value

