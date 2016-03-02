import cmd
import os
import sqlite3
import shutil
import tempfile

from character import Character
import constants
from room import Room
from utilities import term


class Game(object):

    def __init__(self):
        self.character = Character()
        self.loc = Room.get_room(1)
        self.loc.print_room()


class Commands(cmd.Cmd):
    prompt = term.green_on_red('=>')

    def __init__(self):
        cmd.Cmd.__init__(self)

    def move(self, direction):
        newroom = constants.GAME.loc.get_neighbor(direction)
        if newroom is None:
            print("you can't go this way")
        else:
            constants.GAME.loc = Room.get_room(newroom)
            constants.GAME.loc.print_room()

    def do_up(self, args):
        """Go up"""
        self.move('up')

    def do_down(self, args):
        """Go down"""
        self.move('down')

    def do_n(self, args):
        """Go north"""
        self.move('n')

    def do_s(self, args):
        """Go south"""
        self.move('s')

    def do_e(self, args):
        """Go east"""
        self.move('e')

    def do_w(self, args):
        """Go west"""
        self.move('w')

    def do_quit(self, args):
        """Leaves the game"""
        print("Thank you for playing")
        return True

    def do_take(self, args):
        """Takes an item from room and adds it to inventory"""
        constants.GAME.character.take_from_room(constants.GAME.loc, args)

    def do_drop(self, args):
        """Drop item from inventory into room"""
        constants.GAME.character.put_in_room(constants.GAME.loc, args)

    def do_look(self, args):
        if args == 'room':
            constants.GAME.loc.print_room()

    def do_inv(self, args):
        constants.GAME.character.show_inventory()

    def do_save(self, args):
        """save the game"""
        save_path = '../saves/{}'.format(args)
        shutil.copyfile(constants.DBFILE, save_path)
        print("The game was saved to {}".format(save_path))


def prompt_load_game(number_of_saves):
    choice = None
    choices = [str(x + 1) for x in range(number_of_saves)]
    choices.append('N')
    print(choices)
    while choice not in choices:
        choice = input("\nEnter save number or 'N' for a new game: ").upper()
    return choice


def load_database():
    saves = os.listdir('../saves')
    game_file = '../db/game.db'
    if saves:
        print('Do you wish to restore a saved game?')
        print('N: Start a new game.')
        for idx, save in enumerate(saves, 1):
            print('{}:  {}'.format(idx, save))
        load = prompt_load_game(len(saves))
        game_file = '../saves/{}'.format(saves[int(load) - 1]) if load != 'N' else game_file

    dbfile_path = game_file
    constants.DBFILE = tempfile.mktemp()
    shutil.copyfile(dbfile_path, constants.DBFILE)

    constants.DATABASE = sqlite3.connect(constants.DBFILE)


if __name__ == "__main__":
    load_database()
    constants.GAME = Game()
    c = Commands()
    c.cmdloop()
