# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[], is_illuminated=True):
        self.name = name
        self.description = description
        self.items = items
        self.is_illuminated = is_illuminated
