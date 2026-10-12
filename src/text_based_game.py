"""Project Two starter for the student's text-based adventure game."""

# TODO: Add the full-name comment required by Project Two directions.
# Astral Breakout Text Adventure Game
# Jonathan Burney
# Project Two

def show_instructions():
    """Display the game objective and available commands."""
    # TODO: Print instructions that match your game and commands.
    print("\nAstral Breakout")
    print("Collect all 6 items before confronting DANTE.")
    print("Move commands: go north, go south, go east, go west")
    print("Item command: get <item name>")
    pass


def show_status(current_room, inventory, rooms):
    """Display the player's current game status."""
    # TODO: Show the current room.
    # TODO: Show the current inventory.
    # TODO: Show the current-room item when one is available.
     print("\n---------------------------")
    print("Current Location:", current_room)
    print("Inventory:", inventory)

    if "item" in rooms[current_room]:
        print("You see:", rooms[current_room]["item"])

    print("---------------------------")
    pass


def main():
    """Run the main gameplay loop."""
# Dictionary linking rooms and room items
    rooms = {
        'Shuttle Cockpit': {
            'north': 'Communications Hub',
            'east': 'Crew Quarters',
            'south': 'Armory',
            'west': 'Supply Storage'
        },

        'Communications Hub': {
            'south': 'Shuttle Cockpit',
            'east': 'Medical Lab',
            'item': 'radio'
        },

        'Armory': {
            'east': 'Engineering Bay',
            'north': 'Shuttle Cockpit',
            'item': 'plasma shield'
        },

        'Engineering Bay': {
            'west': 'Armory',
            'item': 'repair kit'
        },

        'Supply Storage': {
            'east': 'Shuttle Cockpit',
            'item': 'energy cell'
        },

        'Crew Quarters': {
            'west': 'Shuttle Cockpit',
            'north': 'Control Core',
            'item': 'keycard'
        },

        'Medical Lab': {
            'west': 'Communications Hub',
            'item': 'med pack'
        },

        # Villain room
        'Control Core': {
            'south': 'Crew Quarters',
            'item': 'DANTE'
        }
    }

    # Starting room and inventory
    current_room = 'Shuttle Cockpit'
    inventory = []

    # Number of items required to win
    required_items = 6

    show_instructions()

    # Main gameplay loop
    while True:

        show_status(current_room, inventory, rooms)

        # Check for villain encounter
        if current_room == 'Control Core':

            if len(inventory) == required_items:
                print("\nCongratulations!")
                print("You collected all items and defeated DANTE!")
                print("Thanks for playing Astral Breakout!")
            else:
                print("\nDANTE has overpowered you!")
                print("NOM NOM...GAME OVER!")
                print("Thanks for playing Astral Breakout!")

            break

        # Receive player command
        command = input("\nEnter your move: ").lower().strip()

        # Movement command
        if command.startswith("go "):

            direction = command.split()[1]

            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
                print("You moved to", current_room)

            else:
                print("You can't go that way! Invalid direction.")

        # Item collection command
        elif command.startswith("get "):

            item_requested = command[4:]

            if "item" in rooms[current_room]:

                room_item = rooms[current_room]["item"]

                if item_requested.lower() == room_item.lower():

                    inventory.append(room_item)

                    del rooms[current_room]["item"]

                    print(room_item, "added to inventory.")

                else:
                    print("That item is not in this room.")

            else:
                print("There are no items in this room.")

        # Invalid command
        else:
            print("Invalid command.")
            print("Use:")
            print("go north, go south, go east, go west")
            print("get <item name>")


# Run the game
    pass


if __name__ == "__main__":
    main()
