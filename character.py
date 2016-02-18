class Character(object):

    def __init__(self):
        self.inventory = []

    def take_from_room(self, room, thing):
        try:
            self.inventory.append(thing)
            room.items.remove(thing)
        except ValueError:
            print("You cannot take {}.".format(thing))
        room.save()

    def put_in_room(self, room, thing):
        try:
            room.items.append(thing)
            self.inventory.remove(thing)
        except ValueError:
            print("You do not have {}.".format(thing))
        room.save()

    def show_inventory(self):
        print("Inventory: {}".format(self.inventory))
