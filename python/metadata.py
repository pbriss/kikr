import json
from event import Event

events = list()
events.append(Event(1, 'straight-air', 'Straight air', '18 ft', 218, 228))

print json.dumps(events, default=lambda o: o.__dict__)