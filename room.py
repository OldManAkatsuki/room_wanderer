import json
import sqlite3
from utilities import gprint
from item import Item


class Room():

    cursor = sqlite3.connect("game.db").cursor()

    @classmethod
    def get_room(self, id):
        for row in self.cursor.execute("select json from rooms where id=?", (id,)):
            jsontext = row[0]
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
