"""
Simplified version of 'Battleship' (game),
running in the terminal and featuring 1x1-sized ships.
"""

# Methods imported from built-in modules:
from string import ascii_uppercase
from random import randint

# Global variables:
SCORES = {'computer': 0, 'player': 0}
OUTCOMES = {'hit': True, 'miss': False}


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
        - 2 assigned via methods.
        """
        self.size = size
        self.fleet = fleet
        self.name = name
        self.owner = owner

        self.map = [['□' for x in range(size)] for y in range(size)]
        self.columns_dictionary = dict(zip(ascii_uppercase, range(size)))

        self.ships = []
        self.guesses = []

    def print_map(self):
        """
        Map is printed by writing columns first.
        Then, each row number is followed by a map row.
        """
        print('  ' + ' '.join(list(self.columns_dictionary)))
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
        It assigns the guesses list by appending tuples-based coordinates. It
        then marks the map based on the match between an opponent guess and
        the actual ship position. Finally, it returns an easy-to-read outcome.
        """
        self.guesses.append((row, column))
        self.map[row][column] = 'x'

        if (row, column) in self.ships:
            self.map[row][column] = '#'
            return OUTCOMES['hit']
        else:
            return OUTCOMES['miss']


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
        row, column = randomize(instance.size), randomize(instance.size)

        while (row, column) in instance.ships:
            row, column = randomize(instance.size), randomize(instance.size)

        instance.add_ship(row, column)


# Function handling guesses, accepting a board-instance as a parameter:
def make_guess(instance):
    """
    It handles player's and computer's guesses respectively.
    It leverages the validation function 'validate_guess()'.
    It then provides a written feedback about the guesses outcomes.
    """
    # Player block:
    if instance.owner == 'computer':

        while True:
            row = input(
                f'Guess a row between 0 and {instance.size - 1}: ')
            column = input(
                f'Guess a column between A and '
                f'{list(instance.columns_dictionary)[-1]}: ').upper()

            if validate_guess(row, column, instance):
                break

        print('-' * 34)
        print(f'You guessed: {(int(row), column)}')

        if instance.add_guess(int(row), instance.columns_dictionary[column]):
            print('You got a hit!')
            SCORES['player'] += 1
        else:
            print('You missed this time.')

    # Computer block:
    else:

        row, column = randomize(instance.size), randomize(instance.size)

        while (row, column) in instance.guesses:
            row, column = randomize(instance.size), randomize(instance.size)

        # Ancillary variables:
        letters = list(instance.columns_dictionary.keys())
        numbers = list(instance.columns_dictionary.values())
        # Used in the following print-statement for better readability:

        print('-' * 34)
        print(f'Computer guessed: {(row, letters[numbers.index(column)])}')

        if instance.add_guess(row, column):
            print('Computer got a hit!')
            SCORES['computer'] += 1
        else:
            print('Computer missed this time.')


# Function validating user inputs; board-instance parameter is also needed:
def validate_guess(row, column, instance):
    """
    It validates user inputs by parsing both rows and columns entered.
    """
    # Row/Integer validation block:
    try:
        int(row)
        if int(row) not in range(instance.size):
            raise ValueError(
                f'Your shot has to target the battleground. '
                f'Row {row} is not in the ocean')

    except ValueError as e:
        print(f'Invalid row entered: {e}. Please, try again!')
        return False

    # Column/String validation block:
    if column not in list(instance.columns_dictionary):
        print(
            f'Invalid column entered. '
            f'Column {column} in not in the ocean. Please, try again!')
        return False

    # Guess uniqueness validation block:
    if (int(row), instance.columns_dictionary[column]) in instance.guesses:
        print('Shooting on the same spot more than once? Please, try again!')
        return False

    return True
