# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, location):
        self.is_playing = True
        self.location = location
        self.did_move = True
        self.items = []

    def move(self, direction):
        if hasattr(self.location, direction):
            self.location = getattr(self.location, direction)
            self.did_move = True
        else:
            print("There is nothing in that direction")

    def take(self, item_name):
        if item_name in map(lambda item: item.name, self.location.items):
            print("item is in this location")
