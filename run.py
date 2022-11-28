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


# Function orchestrating the entire game logic:
def run_game(computer_board, player_board):
    """
    It keeps looping its logic, by leveraging the 'make_guess()' function,
    through all the turns needed to reach a game over condition.
    """
    while True:
        print(f'{computer_board.name}'"'s Board:\n")
        computer_board.print_map()
        print(f'\n{player_board.name}'"'s Board:\n")
        player_board.print_map()
        print('-' * 34)

        # Player guessing on computer's board:
        make_guess(computer_board)
        # Computer guessing on player's board:
        make_guess(player_board)

        # Game over conditions:
        winning_condition = all(
            ship in computer_board.guesses for ship in computer_board.ships)
        losing_condition = all(
            ship in player_board.guesses for ship in player_board.ships)

        # Possible turn outcomes:
        if winning_condition is True and losing_condition is False:
            print('-' * 34)
            print('Congratulations! You won the battle!')
            break
        elif winning_condition is False and losing_condition is True:
            print('-' * 34)
            print('You have been defeated! You lost the battle!')
            break
        elif winning_condition is True and losing_condition is True:
            print('-' * 34)
            print('Both the fleets have been sunk! It is a draw!')
            break
        else:
            print('-' * 34)
            print('After this round, the scores are:')
            print(
                f'{player_board.name}:', SCORES['player'],
                '-',
                f'{computer_board.name}:', SCORES['computer'])
            print('-' * 34)

        # Reset and restart option, based on player choice:
        choice = input(
            'Enter any key to continue or "r" to reset and restart the game: ')
        print('-' * 34)

        if choice == 'r':
            initialize_game()

    # Running after a game over condition has been met:
    input('Press any key to start a new game: ')
    initialize_game()


# Function starting new games:
def initialize_game():
    """
    It resets points (player's, computer's), initializes boards,
    calls the 'run_game()' function.
    """
    SCORES['computer'] = 0
    SCORES['player'] = 0

    # Size has been set to 5 because of the presence of 1x1 ships:
    size = 5
    fleet = 5

    # Game presentation:
    print('-' * 34)
    print('Welcome to BATTLESHIP CHALLENGE!')
    print(f'Board Size: {size} x {size}. Ships: {fleet} each.')
    print('-' * 34)

    player_name = input('Please, enter your name:\n')
    print('-' * 34)

    # Class instances:
    computer_board = Board(size, fleet, 'Computer', owner='computer')
    player_board = Board(size, fleet, player_name, owner='player')

    # Function calls to create the fleets:
    populate_map(computer_board)
    populate_map(player_board)

    # Function call to manage the game:
    run_game(computer_board, player_board)


initialize_game()
