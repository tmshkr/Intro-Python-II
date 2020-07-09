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
