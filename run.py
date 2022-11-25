"""
Simplified version of 'Battleship' (game),
running in the terminal and featuring 1x1-sized ships.
"""

# Methods imported from modules:
from string import ascii_uppercase
from random import randint

# Global variables:
OUTCOMES = ('Hit!', 'Miss!')
SCORES = {'computer': 0, 'player': 0}


# Board class, representing the parent class for boards:
class Board:
    """
    It sets the board sizes, the number of ships (fleet),
    the player's name and the board owner (player, computer).
    It has methods for printing maps (player's, computer's),
    adding its own ships and opponent's guesses.
    """

    def __init__(self, size, fleet, name, owner):
        """
        Instance attributes:
        - 4 assigned via parameterization;
        - 2 derived from a parameter;
        - 1 derived from another;
        - 2 assigned via methods.
        """
        self.size = size
        self.fleet = fleet
        self.name = name
        self.owner = owner

        self.map = [['□' for x in range(size)] for y in range(size)]
        self.columns_dictionary = dict(zip(ascii_uppercase, range(size)))

        self.columns_string = '  ' + ' '.join(list(self.columns_dictionary))

        self.ships = []
        self.guesses = []

    def print_map(self):
        """
        Map is printed by writing columns first.
        Then, each row number is followed by a map row.
        """
        print(self.columns_string)
        row_number = 0

        for row in self.map:
            print(f"{row_number} {' '.join(row)}")
            row_number += 1

    def add_ship(self, row, column):
        """
        It assignes the ships list by appending tuples-based coordinates.
        Ships on player's map are made visible by using distinctive markers.
        """
        self.ships.append((row, column))

        if self.owner == 'player':
            self.map[row][column] = '■'

    def add_guess(self, row, column):
        """
        It assigns the guesses list by appending tuples-based coordinates.
        It then marks the map based on the match between an opponent guess
        and the actual ship position. Finally, it returns an outcome.
        """
        self.guesses.append((row, column))
        self.map[row][column] = 'x'

        if (row, column) in self.ships:
            self.map[row][column] = '#'
            return OUTCOMES[0]
        else:
            return OUTCOMES[1]


# Helper function returning a random integer between 0 and size:
def randomize(size):
    """
    It generates a random coordinate by leveraging the 'randint()' method.
    """
    return randint(0, size - 1)


# Function randomly populating maps, accepting a board-instance as a parameter:
def populate_map(instance):
    """
    It leverages the helper function 'randomize()',
    by also ensuring that any assignment to the ships list is unique.
    """
    for i in range(instance.fleet):
        row, column = randomize(instance.size),
        randomize(instance.size)

        while (row, column) in instance.ships:
            row, column = randomize(instance.size),
            randomize(board_instance.size)

        instance.add_ship(row, column)
