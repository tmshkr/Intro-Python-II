class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def describe(self):
        print(self.description)
