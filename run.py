"""
Simplified version of 'Battleship' (game),
running in the terminal and featuring 1x1-sized ships.
"""

# Importing of common tools needed in the following:
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
        print(self.columns_string)
        row_number = 0

        for row in self.board:
            print('%d %s' % (row_number, ' '.join(row)))
            row_number += 1

    def add_ship(self, row, column):
        self.ships.append((row, column))

        if self.type == 'player':
            self.board[row][column] = '■'

    def add_guess(self, row, column):
        self.guesses.append((row, column))
        self.board[row][column] = 'x'

        if (row, column) in self.ships:
            self.board[row][column] = '#'
            return OUTCOMES[0]
        else:
            return OUTCOMES[1]
