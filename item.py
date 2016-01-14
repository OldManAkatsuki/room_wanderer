import json
import sqlite3
from utilities import gprint


class Item():

    @staticmethod
    def get_item(name):
        con = sqlite3.connect("game.db")
        jsontext = con.execute("select json from items where name=?", (name,)).fetchone()[0]
        con.close()
        d = json.loads(jsontext)
        d['id'] = id
        return Item(**d)

    def __init__(self, id=0, name=None, description=None):
        self.id = id
        self.name = name
        self.description = description

    def print_item(self):
        gprint('{}: {}'.format(self.name, self.description))
