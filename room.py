import json
import sqlite3
from utilities import gprint, gprint_color


class Room():

    @staticmethod
    def get_room(id):
        con = sqlite3.connect("game.db")
        for row in con.execute("select json from rooms where id=?", (id,)):
            jsontext = row[0]
            d = json.loads(jsontext)
            d['id'] = id
            return Room(**d)

    def __init__(self, id=0, name="A Room", description="An empty room", neighbors={}):
        self.id = id
        self.name = name
        self.description = description
        self.neighbors = neighbors

    def get_neighbor(self, direction):
        if direction in self.neighbors:
            return self.neighbors[direction]
        else:
            return None

    def print_room(self):
        gprint_color(self.name, 'bold_red_on_white')
        print("")
        gprint(self.description)
