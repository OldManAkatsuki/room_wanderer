import unittest
from item import Item
from io import StringIO
import json
from contextlib import redirect_stdout
import sqlite3


class ItemTests(unittest.TestCase):

    def test_creat_item_with_defaults(self):
        item = Item()
        self.assertEqual(item.name, None)
        self.assertEqual(item.description, None)

    def test_create_item_with_parameters(self):
        item = Item(name='cat', description='test')
        self.assertEqual(item.name, 'cat')
        self.assertEqual(item.description, 'test')

    def test_print_item(self):
        item = Item(name='cat', description='test')
        output = StringIO()
        with redirect_stdout(output):
            item.print_item()
        self.assertEqual('     cat: test\n', output.getvalue())

    def test_get_item(self):
        file_name = 'cat'
        item_json = json.dumps({
            'name': 'cat',
            'description': 'cute'
        })
        con = sqlite3.connect(':memory:')
        con.execute("CREATE TABLE IF NOT EXISTS items(id INTEGER PRIMARY KEY, name TEXT NOT NULL, json TEXT NOT NULL)")
        con.commit()
        con.execute("INSERT OR REPLACE INTO items(name, json) VALUES(?, ?);", (file_name, item_json))
        con.commit()
        item = Item.get_item('cat', con)
        self.assertEqual(item.name, 'cat')
        self.assertEqual(item.description, 'cute')
        con.close()


if __name__ == '__main__':
    unittest.main()
