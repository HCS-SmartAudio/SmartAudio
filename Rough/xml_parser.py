import os
import xml.etree.cElementTree as ET
from util.test_util import TestUtil

current_folder_path = os.path.split(os.getcwd())
print(current_folder_path[0]+"\Resources\EventKeyList.xml")
key = "power on"
k1 = key.split(" ")
print(k1[0])

DOMTree =ET.parse(current_folder_path[0]+"\Resources\EventKeyList.xml")
itemList = DOMTree.getroot()
print(itemList.tag)
for child_of_root in itemList:
    print(child_of_root.tag, child_of_root.attrib)

for elem in itemList.findall("./"+k1[0]+"/"+k1[1]):
    print(elem.attrib, elem.text)

ss = TestUtil()
ss.search_for_event_id("power on")
print(ss.search_for_event_id("power on"))
print(ss.search_for_event_value("power on"))
