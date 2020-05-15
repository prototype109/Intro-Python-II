from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

room['outside'].items = [Item('Knife', 'stabby stabby')]
room['foyer'].items = [Item('Book', 'smarts')]
room['overlook'].items = [Item('Health Kit', 'unbreak my heart')]
room['narrow'].items = [Item('Bed', 'You wake up in minecraft')]
room['treasure'].items = [Item('Box', 'What is in')]

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Noob', room['outside'])

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

def attempt_move(direction_input):
    directions = {
        "n":("n_to", "north"),
        "e":("e_to", "east"),
        "s":("s_to", "south"),
        "w":("w_to", "west"),
    }

    if direction_input.lower() == 'q' or direction_input.lower() == 'quit':
        return False

    possible_room = player.current_room.__getattribute__(directions[direction_input][0])

    if  possible_room != None:
        player.current_room = possible_room
    else:
        print(f'''
            ----------------------------------------------

            there is no available room to the {directions[direction_input][1]}
            ----------------------------------------------
        ''')
    return True


continue_adventure = True

while continue_adventure:
    print(player)
    print(player.current_room)
    selection = input(
        '''Please select direction that you would like to go in
        n - North
        e - East
        s - South
        w - West
        ________________________________________________________
        i, inventory - inventory
        q, quit - Quit
        ''').split(' ')
    
    if len(selection) > 1:
        if selection[0] == 'take':
            player.take_item(selection[1])
        elif selection[0] == 'drop':
            player.drop_item(selection[1])
    else:
        if selection[0] == 'i' or selection[0] == 'inventory':
            player.show_inventory()
        else:
            continue_adventure = attempt_move(selection[0])
    

