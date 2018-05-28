import re

from util.event_handler import EventHandler

data1 = 'Check the system can enter on mode by the following case: Power on from off mode by pressing power button'
tu = EventHandler()
el = tu.search_for_event_key(data1)
print(tu.search_for_event_value(el))
print(tu.search_for_event_id(el))



