# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items

    def describe(self):
        print(f"Current location: {self.name}")
        print(self.description.replace("\n", " "))
        print()

        num_items = len(self.items)
        if num_items == 1:
            print("There is an item visible:")
        elif num_items > 1:
            print(f"There are {num_items} visible:")
        for item in self.items:
            item.describe()
        if num_items > 0:
            print()

        if hasattr(self, "n"):
            name = getattr(self, "n").name
            print(f"To the North: {name}")
        if hasattr(self, "s"):
            name = getattr(self, "s").name
            print(f"To the South: {name}")
        if hasattr(self, "e"):
            name = getattr(self, "e").name
            print(f"To the East: {name}")
        if hasattr(self, "w"):
            name = getattr(self, "w").name
            print(f"To the West: {name}")
