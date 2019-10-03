# Write a class to hold player information, e.g. what room they are in
# currently.
# This holds what room they are in!!
# Should have inventory, health, ect


class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def move_player(self, dir):
        if dir == 'n':
            self.current_room = self.current_room.n_to
        elif dir == 'e':
            self.current_room = self.current_room.e_to
        elif dir == 's':
            self.current_room = self.current_room.s_to
        elif dir == 'w':
            self.current_room = self.current_room.w_to
    
    def take_item(self, item):
        # self.inventory = self.inventory.append(item)
        print(f'You picked up a(n) {item}')
    def drop_item(self, item):
        print(f'You dropped the {item}')


    def __str__(self):
        return f'\nRoom:{self.current_room} \n'
    


# p = Player("Micah", "Living Room")
# print(p)
