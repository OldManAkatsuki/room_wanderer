import json

import constants
from utilities import gprint


class Item():

    @staticmethod
    def get_item(name):
        jsontext = constants.DATABASE.execute("select json from items where name=?", (name,)).fetchone()[0]
        d = json.loads(jsontext)
        return Item(**d)

    def __init__(self, name=None, description=None):
        self.name = name
        self.description = description

    def print_item(self):
        gprint('{}: {}'.format(self.name, self.description))
