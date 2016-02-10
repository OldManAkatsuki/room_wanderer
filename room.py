import json

import constants
from item import Item
from utilities import gprint


class Room():

    @staticmethod
    def get_room(id):
        jsontext = constants.DATABASE.execute("select json from rooms where id=?", (id,)).fetchone()[0]
        d = json.loads(jsontext)
        d['id'] = id
        return Room(**d)

    def __init__(self, id=0, name="A Room", description="An empty room", neighbors={}, items=[]):
        self.id = id
        self.name = name
        self.description = description
        self.neighbors = neighbors
        self.items = items

    def get_neighbor(self, direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None

    def print_room(self):
        gprint(self.name, 'bold_red_on_white')
        print("")
        gprint(self.description)
        print("")
        gprint('items:')
        for item in self.items:
            Item.get_item(item).print_item()

    def save(self):
        room_json = json.dumps({
            'name': self.name,
            'description': self.description,
            'neighbors': self.neighbors,
            'items': self.items
        })
        constants.DATABASE.execute("INSERT OR REPLACE INTO rooms(id, json) VALUES(?, ?);", (self.id, room_json))
        constants.DATABASE.commit()
