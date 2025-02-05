# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = items

    def __str__(self):
        return f' {self.name} - {self.description}'


# r = Room("Living Room", "A quaint room with a piano")
#  - Looking around you see a: {self.items}
# print(r)
