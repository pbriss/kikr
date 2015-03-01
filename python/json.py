import json
from event import Event

events = list()
events.append(Event(5, 9))

print json.dumps(events, default=lambda o: o.__dict__)
