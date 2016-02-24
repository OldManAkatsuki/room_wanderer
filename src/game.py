import cmd
import sqlite3
import shutil
import tempfile

from character import Character
import constants
from room import Room
from utilities import term


class Game(cmd.Cmd):
    prompt = term.green_on_red('=>')

    def __init__(self, db=None, dbfile='../db/game.db'):
        cmd.Cmd.__init__(self)

        self.character = Character()
        self.loc = Room.get_room(1)
        self.loc.print_room()

    def move(self, direction):
        newroom = self.loc.get_neighbor(direction)
        if newroom is None:
            print("you can't go this way")
        else:
            self.loc = Room.get_room(newroom)
            self.loc.print_room()

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
        self.character.take_from_room(self.loc, args)

    def do_drop(self, args):
        """Drop item from inventory into room"""
        self.character.put_in_room(self.loc, args)

    def do_look(self, args):
        if args == 'room':
            self.loc.print_room()

    def do_inv(self, args):
        self.character.show_inventory()

    def do_save(self, args):
        """save the game"""
        save_path = '../saves/{}'.format(args)
        shutil.copyfile(constants.DBFILE, save_path)
        print("The game was saved to {}".format(save_path))

if __name__ == "__main__":
    dbfile_path = '../db/game.db'
    constants.DBFILE = tempfile.mktemp()
    shutil.copyfile(dbfile_path, constants.DBFILE)

    constants.DATABASE = sqlite3.connect(constants.DBFILE)

    g = Game()
    g.cmdloop()
