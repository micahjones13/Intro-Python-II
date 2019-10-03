from room import Room
from player import Player
from item import Item
import sys
#Declare the items


items = {
   'letter': Item("letter", "It reads 'Leap', and that's it."),
    'sword': Item("sword", "It's steel has been blunted over the years"),
    'pebbles': Item("pebbles", "Some ordinary pebbles"),
    'shield': Item("sheild", "This will protect you"),
   'goblet': Item("goblet", "It has a strange language on it"),
}
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [items["letter"]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [items["sword"]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items["pebbles"]]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [items["shield"]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items["goblet"]]),
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

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
name = input("What's your name?: ")
new_player = Player(name, room['outside'])
# print(new_player)
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


quit = False
while quit == False:
    print(new_player)
    if len(new_player.current_room.items) > 0:
        print("Looking around, you see a: ", end='')
        for i in new_player.current_room.items:
            print(i.name)
    user_input = input("what will you do? (n, e, s, w, take, drop): ")
    input_length = user_input.split()
    if len(input_length) == 1:
        
        if user_input == 'q':
            print('Thanks for playing!')
            break
        elif user_input == 'n':
            if new_player.current_room.n_to == None:
                print("You cannot move that direction")
            else:
                new_player.move_player(user_input)
        elif user_input == 'e':
            if new_player.current_room.e_to == None:
                print("You cannot move that direction")
            else:
                new_player.move_player(user_input)
        elif user_input == 's':
            if new_player.current_room.s_to == None:
                print("You cannot move that direction")
            else:
                new_player.move_player(user_input)
        elif user_input == 'w':
            if new_player.current_room.w_to == None:
                print("You cannot move that direction")
            else:
                new_player.move_player(user_input)
        else:
            print('Not valid input. please use n, e, s, w for direcitonal movement.')
    elif len(input_length) == 2:
        #if there is an item in the room, and player says take (item), call take_item from player
        if 'take' in user_input:
            # print('take')
            # print(new_player.current_room.items)
            input_item_name = user_input[5:]
            for item in new_player.current_room.items:
                if item.name == input_item_name:
                    print(f'you take the {item.name}')
                    new_player.take_item(item)
                    # print(item, 'what item looks like')
                    # !Must loop through inventory to avoid getting the obejct at memory
                    new_player.inventory.append(items[input_item_name])
                    new_player.current_room.items.remove(items[input_item_name])
                else:
                    print('That item is not here')
        elif 'drop' in user_input:
            input_item_name = user_input[5:]
            new_player.drop_item(input_item_name)
            new_player.inventory.remove(items[input_item_name])
            print(new_player.inventory, 'player inv after drop')
            #add item to room it was dropped at
            new_player.current_room.items.append(items[input_item_name])
            
        else:
            print('not valid command')
    else:
        break
