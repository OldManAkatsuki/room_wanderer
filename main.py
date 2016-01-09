import cmd
from room import get_room


class Game(cmd.Cmd):
    prompt = '^_^ >'

    def __init__(self):
        cmd.Cmd.__init__(self)

        self.loc = get_room(1)
        self.loc.print_room()

    def move(self, direction):
        newroom = self.loc.get_neighbor(direction)
        if newroom is None:
            print("you can't go this way")
        else:
            self.loc = get_room(newroom)
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


if __name__ == "__main__":
    g = Game()
    g.cmdloop()
