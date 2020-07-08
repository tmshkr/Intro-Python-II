# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, location):
        self.is_playing = True
        self.location = location
        self.did_err = False

    def move(self, direction):
        if hasattr(self.location, direction):
            self.location = getattr(self.location, direction)
        else:
            self.did_err = True
            print("There is nothing in that direction")
