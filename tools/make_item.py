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


def get_item_info():
    file_name = input('File Name: ')
    item_name = input('Item Name: ')
    short_desc = input('Short Description: ')
    long_desc = input('Long Description: ')
    return (
        file_name,
        {
            'name': item_name,
            'short_description': short_desc,
            'long_description': long_desc
        }
    )


def confirm_entry(data):
    print('\n\n')
    print('The item you entered: ')
    print(json_data)
    confirm = None
    while confirm not in ['Y', 'N']:
        confirm = input('\nIs this correct? (y/n) >').upper()
    return confirm == 'Y'


file_name, data = get_item_info()
json_data = json.dumps(data, indent=3)
if confirm_entry(json_data):
    with open('{}/{}.json'.format(item_path, file_name), 'w') as f:
        f.write(json_data)
