from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room(
        "Outside Cave Entrance",
        "North of you, the cave mount beckons", [
            Item("stone", "a smooth and round stone")
        ]),

    'foyer':    Room(
        "Foyer",
        """Dim light filters in from the south. Dusty
passages run north and east.""", [
            Item("lantern", "an old lantern, seems to have been used recently"),
            Item("oil", "a canister of oil, perhaps for the lantern")]
    ),

    'overlook': Room(
        "Grand Overlook",
        """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""
    ),

    'narrow':   Room(
        "Narrow Passage",
        """The narrow passage bends here from west
to north. The smell of gold permeates the air."""
    ),

    'treasure': Room(
        "Treasure Chamber",
        """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [
            Item("map", "a treasure map"),
            Item("compass", "a compass, with an indiscernible inscription")
        ]),
}


# Link rooms together

room['outside'].n = room['foyer']
room['foyer'].s = room['outside']
room['foyer'].n = room['overlook']
room['foyer'].e = room['narrow']
room['overlook'].s = room['foyer']
room['narrow'].w = room['foyer']
room['narrow'].n = room['treasure']
room['treasure'].s = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
p = Player(room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
print("Enter 'help' for a list of commands")
while p.is_playing:
    if p.did_move:
        p.location.describe()
        p.did_move = False

    user_input = input(
        "\n\033[1mWhat do you want to do?\033[0m ").lower().split(" ")
    print("")

    if len(user_input) == 1:
        user_input = user_input[0]
        if user_input == "help":
            print(
                "n: move north\n"
                "s: move south\n"
                "e: move east\n"
                "w: move west\n"
                "d: describe location\n"
                "get [item_name]: pick up an item\n"
                "drop [item_name]: drop an item\n"
                "i: list items in your inventory\n"
                "q: quit game\n"
            )

        elif user_input in ["n", "s", "e", "w"]:
            p.move(user_input)

        elif user_input == "d":
            p.location.describe()

        elif user_input in ["i", "inventory"]:
            p.inventory()

        elif user_input == "q":
            p.is_playing = False
            print("Goodbye")

        else:
            print("Invalid input")

    elif len(user_input) == 2:
        if user_input[0] in ["get", "take"]:
            p.take(user_input[1])

        elif user_input[0] == "drop":
            p.drop(user_input[1])

        else:
            print("Invalid input")

    else:
        print("Invalid input")
