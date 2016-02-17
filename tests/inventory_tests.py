from contextlib import redirect_stdout
from io import StringIO
import json
import sqlite3
import unittest

from game import Game
from room import Room


class InventoryIntegrationTests(unittest.TestCase):

    def test_get_item_from_room_adds_to_inventory_and_removes_from_room(self):
        con = sqlite3.connect(':memory:')
        self.create_room(con, items=['BFG9000'])
        self.create_item(con, name='BFG9000')
        output = StringIO()
        with redirect_stdout(output):
            game = Game(db=con)
        # room in database has item persisted
        room = Room.get_room(1)
        self.assertEqual(room.items, ['BFG9000'])
        # inventory is empty
        self.assertEqual(game.character.inventory, [])
        # room in game object has items fetched from db
        self.assertEqual(game.loc.items, ['BFG9000'])
        # take item from room, add to character's inventory
        game.character.take_from_room(game.loc, 'BFG9000')
        # character's inventory now has item
        self.assertEqual(game.character.inventory, ['BFG9000'])
        # room in game object no longer has item
        self.assertEqual(game.loc.items, [])
        # room in database is persisted without item
        room = Room.get_room(1)
        self.assertEqual(room.items, [])

    def test_cannot_take_item_that_does_not_exist(self):
        con = sqlite3.connect(':memory:')
        self.create_room(con, items=['BFG9000'])
        self.create_item(con, name='BFG9000')
        with redirect_stdout(StringIO()):
            game = Game(db=con)
        output = StringIO()
        with redirect_stdout(output):
            game.character.take_from_room(game.loc, 'cat')
        self.assertEqual(output.getvalue(), 'You cannot take that.\n')

    def test_put_item_in_room_removes_from_inventory_and_adds_to_room(self):
        con = sqlite3.connect(':memory:')
        self.create_room(con, items=[])
        self.create_item(con, name='BFG9000')
        output = StringIO()
        with redirect_stdout(output):
            game = Game(db=con)
        game.character.inventory = ['BFG9000']
        # room in database has item persisted
        room = Room.get_room(1)
        self.assertEqual(room.items, [])
        # inventory has our item
        self.assertEqual(game.character.inventory, ['BFG9000'])
        # room in game object has items fetched from db
        self.assertEqual(game.loc.items, [])
        # take item from inventory, add to room
        game.character.put_in_room(game.loc, 'BFG9000')
        # character's inventory now is empty
        self.assertEqual(game.character.inventory, [])
        # room in game object now has item
        self.assertEqual(game.loc.items, ['BFG9000'])
        # room in database is persisted withitem
        room = Room.get_room(1)
        self.assertEqual(room.items, ['BFG9000'])

    def test_cannot_drop_an_item_that_you_do_not_have(self):
        con = sqlite3.connect(':memory:')
        self.create_room(con, items=[])
        self.create_item(con, name='BFG9000')
        with redirect_stdout(StringIO()):
            game = Game(db=con)
        output = StringIO()
        with redirect_stdout(output):
            game.character.put_in_room(game.loc, 'BFG9000 cat')
        self.assertEqual(output.getvalue(), 'You do not have that.\n')

    def create_room(self, con, items=[]):
        room_json = json.dumps({
            'name': 'room1',
            'description': 'test room',
            'neighbors': {},
            'items': items
        })
        con.execute("CREATE TABLE IF NOT EXISTS rooms(id INTEGER PRIMARY KEY, json TEXT NOT NULL)")
        con.commit()
        con.execute("INSERT OR REPLACE INTO rooms(id, json) VALUES(?, ?);", (1, room_json))
        con.commit()

    def create_item(self, con, name='item'):
        file_name = name
        item_json = json.dumps({
            'name': name,
            'description': 'cute'
        })
        con.execute("CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY, name TEXT NOT NULL, json TEXT NOT NULL)")
        con.commit()
        con.execute("INSERT OR REPLACE INTO items(name, json) VALUES(?, ?);", (file_name, item_json))
        con.commit()
