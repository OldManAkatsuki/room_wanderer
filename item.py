import json
import sqlite3
from utilities import gprint


class Item():

    @staticmethod
    def get_item(name, con=None, db_file='game.db'):
        if not con:
            con = sqlite3.connect(db_file)
        jsontext = con.execute("select json from items where name=?", (name,)).fetchone()[0]
        con.close()
        d = json.loads(jsontext)
        return Item(**d)

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    def print_item(self):
        gprint('{}: {}'.format(self.name, self.description))
