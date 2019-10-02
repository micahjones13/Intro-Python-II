# Write a class to hold player information, e.g. what room they are in
# currently.
# This holds what room they are in!!
# Should have inventory, health, ect


class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f'{self.name}, You are{self.current_room}. inventory: {self.inventory}'


# p = Player("Micah", "Living Room")
# print(p)
