def createItem(name, desciption):
    if name == "lantern":
        return LightSource(name, desciption)
    else:
        return Item(name, desciption)


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def describe(self):
        print("*", self.description.replace(
            self.name,
            f"\033[1m\033[91m{self.name}\033[0m")
        )

    def on_take(self):
        print(f"You have picked up {self.name}")

    def on_drop(self):
        print(f"You have dropped {self.name}")

    def use(self):
        print(f"use {self.name}")


class LightSource(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def on_drop(self):
        print("It's not wise to drop your source of light!")

    def use(self):
        print("use LightSource")
