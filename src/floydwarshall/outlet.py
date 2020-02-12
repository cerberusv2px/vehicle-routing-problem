import json


class Outlet:
    def __init__(self, id, name, latitude, longitude, sequence=0):
        self.id = id
        self.name = name
        self.lat = latitude
        self.lng = longitude
        self.sequence = sequence

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=False, indent=2)
