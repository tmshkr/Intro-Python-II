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
        for index, item in enumerate(self.location.items):
            if item.name == item_name:
                self.items.append(item)
                self.location.items.pop(index)
                print(f"You took the {item_name}")
                return
        print(f"There is no {item_name} here")
