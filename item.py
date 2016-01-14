import json
import sqlite3
from utilities import gprint


class Item():

    cursor = sqlite3.connect("game.db").cursor()

    @classmethod
    def get_item(self, name):
        for row in self.cursor.execute("select json from items where name=?", (name,)):
            jsontext = row[0]
            d = json.loads(jsontext)
            d['id'] = id
            return Item(**d)

    def __init__(self, id=0, name=None, description=None):
        self.id = id
        self.name = name
        self.description = description

    def print_item(self):
        gprint('{}: {}'.format(self.name, self.description))
