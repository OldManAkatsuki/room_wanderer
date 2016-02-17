class Character(object):

    def __init__(self):
        self.inventory = []

    def take_from_room(self, room, thing):
        self.inventory.append(thing)
        room.items.remove(thing)
        room.save()

    def put_in_room(self, room, thing):
        room.items.append(thing)
        room.save()
        self.inventory.remove(thing)
