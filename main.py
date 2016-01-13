import cmd
from room import Room
# from utilities import term
import shutil
import tempfile


class Game(cmd.Cmd):
    prompt = '=>'   # term.green_on_red('=>')

    def __init__(self):
        cmd.Cmd.__init__(self)

        self.loc = Room.get_room(1)
        self.loc.print_room()
        self.dbfile = tempfile.mktemp()
        shutil.copyfile("game.db", self.dbfile)

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

    def do_save(self, args):
        """save the game"""
        shutil.copyfile(self.dbfile, args)
        print("The game was saved to {}".format(args))

if __name__ == "__main__":
    g = Game()
    g.cmdloop()
