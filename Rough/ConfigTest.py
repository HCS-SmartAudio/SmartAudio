import ConfigParser
import os

config = ConfigParser.ConfigParser()
current_folder_path = os.path.split(os.getcwd())
config.read(current_folder_path[0]+"\Properties\Config.properties")

print(config.get('FileSection', 'EventKeyFileLocation'))