"""Module Six Milestone starter for the simplified movement prototype."""
 Astral Breakout
# Jonathan Burney
# Milestone: Move Between Rooms

# Dictionary linking rooms together
rooms = {
    'Shuttle Cockpit': {
        'north': 'Communications Hub',
        'east': 'Crew Quarters',
        'south': 'Armory',
        'west': 'Supply Storage'
    },
    'Communications Hub': {
        'south': 'Shuttle Cockpit',
        'east': 'Medical Lab'
    },
    'Armory': {
        'north': 'Shuttle Cockpit',
        'east': 'Engineering Bay'
    },
    'Engineering Bay': {
        'west': 'Armory'
    },
    'Supply Storage': {
        'east': 'Shuttle Cockpit'
    },
    'Crew Quarters': {
        'west': 'Shuttle Cockpit',
        'north': 'Control Core'
    },
    'Medical Lab': {
        'west': 'Communications Hub'
    },
    'Control Core': {
        'south': 'Crew Quarters'
    }
}

# Starting room
current_room = 'Shuttle Cockpit'

print("Welcome to Astral Breakout!")
print("Move commands: go north, go south, go east, go west")
print('Type "exit" to leave the game.')

# Gameplay loop
while current_room != 'exit':

    print("\nYou are in the", current_room)

    command = input("Enter your move: ").lower().strip()

    # Exit command
    if command == 'exit':
        current_room = 'exit'

    # Movement commands
    elif command.startswith("go "):
        direction = command.split()[1]

        if direction in rooms[current_room]:
            current_room: str = rooms[current_room][direction]
            print("You moved to", current_room)
        else:
            print("You can't go that way.")

    # Invalid command
    else:
        print("Invalid command.")
        print("Use: go north, go south, go east, go west, or exit")

print("\nThanks for playing Astral Breakout!")
