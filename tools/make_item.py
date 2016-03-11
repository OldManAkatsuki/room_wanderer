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
ITEM_NAMES = []
ITEMS = {}

def current_items():
    files = []
    for (dirpath, dirnames, filenames) in os.walk(item_path):
        files.extend(filenames)
        break
    for path in files: 
        with open(os.path.join(item_path, path), "r") as f:
            file_data = json.loads(f.read())
        ITEMS[file_data["name"]] = (path, file_data)
    ITEM_NAMES.extend(sorted(ITEMS.keys()))  


def show_details():
    choice = int(input('What item do you want details for? >>'))
    item = ITEMS[ITEM_NAMES[choice - 1]]
    print('{:>20}: {}'.format('Name', item[1]['name']))    
    print('{:>20}: {}'.format('Short Description', item[1]['short_description'])) 
    print('{:>20}: {}'.format('Long Description',item[1]['long_description']))
    print('{:>20}: {}'.format('Filename', item[0]))  


def display_current_items():
    for idx, item in enumerate(ITEM_NAMES, 1):
        print('{}: {}'.format(idx, item))


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


def make_item():
    file_name, data = get_item_info()
    json_data = json.dumps(data, indent=3)
    if confirm_entry(json_data):
        with open('{}/{}.json'.format(item_path, file_name), 'w') as f:
            f.write(json_data)


def menu():
    quit = False
    while not quit:
        print('\n\nPlease choose an action from the following list:')
        for idx, action in enumerate(ACTIONS, 1):
            print('{}: {}'.format(idx, action[0]))
        print('Q: Quit')
        choice = input('Choice >>').upper()
        if choice == 'Q':
            break
        ACTIONS[int(choice) - 1][1]()


ACTIONS = [
    ('List current items', display_current_items),
    ('Add an item', make_item),
    ('Show details', show_details),
]

current_items()
menu()

