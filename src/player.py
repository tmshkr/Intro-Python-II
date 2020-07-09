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
                item.on_take()
                return
        print(f"There is no {item_name} here")

    def drop(self, item_name):
        for index, item in enumerate(self.items):
            if item.name == item_name:
                self.location.items.append(item)
                self.items.pop(index)
                item.on_drop()
                return
        print(f"There is no {item_name} in your inventory")

    def use_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                item.use()
                return
        print(f"There is no {item_name} in your inventory")

    def inventory(self):
        if len(self.items) > 0:
            print("You have these items in your inventory:")
            for item in self.items:
                print(
                    f"* \033[1m\033[91m{item.name}\033[0m {item.description}")
        else:
            print("You don't have any items in your inventory")

    def describe_location(self):
        location = self.location
        if not location.is_illuminated:
            light_sources = filter(
                lambda i: i.__class__.__name__ == "LightSource" and i.is_illuminated, self.items)
            if len(list(light_sources)) == 0:
                print("It's pitch black!")
                return

        print(f"Current location: {location.name}")
        print(location.description.replace("\n", " "))
        print()

        num_items = len(location.items)
        if num_items == 1:
            print("There is an item visible:")
        elif num_items > 1:
            print(f"There are {num_items} items visible:")
        for item in location.items:
            item.describe()
        if num_items > 0:
            print()

        if hasattr(location, "n"):
            name = getattr(location, "n").name
            print(f"To the North: {name}")
        if hasattr(location, "s"):
            name = getattr(location, "s").name
            print(f"To the South: {name}")
        if hasattr(location, "e"):
            name = getattr(location, "e").name
            print(f"To the East: {name}")
        if hasattr(location, "w"):
            name = getattr(location, "w").name
            print(f"To the West: {name}")
