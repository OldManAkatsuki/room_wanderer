# encoding: utf-8

"""
    [ ] menu options
        [ ] list existing items
        [ ] inspect existing items
        [ ] edit an item
    [√] save item  @done (03/01/16 22:00)
"""
import json
import os

item_path = os.path.relpath('../data/items_new')

file_name = input('File Name: ')
item_name = input('Item Name: ')
short_desc = input('Short Description: ')
long_desc = input('Long Description: ')

data = {
    'name': item_name,
    'short_description': short_desc,
    'long_description': long_desc
}

json_data = json.dumps(data)

with open('{}/{}.json'.format(item_path, file_name), 'w') as f:
    f.write(json_data)
