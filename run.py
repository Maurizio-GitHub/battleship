"""
Simplified version of 'Battleship' (game),
running in the terminal and featuring 1x1-sized ships.
"""

# Importing of methods from modules:
from string import ascii_uppercase
from random import randint

# Global variables:
OUTCOMES = ('Hit!', 'Miss!')
SCORES = {'computer': 0, 'player': 0}


# Board class, representing the parent class for boards:
class Board:
    """
    It sets the board sizes, the number of ships (fleet),
    the player's name and the board type (player's, computer's).
    It has methods for printing boards (player's, computer's),
    adding its own ships and opponent's guesses.
    """

    def __init__(self, size, fleet, name, type):
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
        self.type = type

        self.board = [['□' for x in range(size)] for y in range(size)]
        self.columns_dictionary = dict(zip(ascii_uppercase, range(size)))

        self.columns_string = '  ' + ' '.join(list(self.columns_dictionary))

        self.ships = []
        self.guesses = []

    def print_board(self):
        """
        Board is printed by writing columns first.
        Then, each row number is followed by board rows.
        """
        print(self.columns_string)
        row_number = 0

        for row in self.board:
            print(f"{row_number} {' '.join(row)}")
            row_number += 1

    def add_ship(self, row, column):
        """
        It assignes the ships list by appending tuples-based coordinates.
        Ships on players' boards are made visible by using distinctive markers.
        """
        self.ships.append((row, column))

        if self.type == 'player':
            self.board[row][column] = '■'

    def add_guess(self, row, column):
        """
        It assignes the guesses list by appending tuples-based coordinates. It
        then marks the boards based on the match between a guess and the
        actual ship position. Finally, it returns an outcome.
        """
        self.guesses.append((row, column))
        self.board[row][column] = 'x'

        if (row, column) in self.ships:
            self.board[row][column] = '#'
            return OUTCOMES[0]
        else:
            return OUTCOMES[1]
