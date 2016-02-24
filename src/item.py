import json

import constants
from utilities import gprint, gprint_colorize


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
        name = gprint_colorize(self.name, color='blue')
        gprint('{}: {}'.format(name, self.description))

    @property
    def string(self):
        name = gprint_colorize(self.name, color='blue')
        return '{}: {}'.format(name, self.description)
