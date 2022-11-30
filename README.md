# Battleship Challenge

Battleship Challenge is a Python-terminal game running in the Code Institute mock terminal on Heroku.

It represents a simplified version of the original game, as each battleship occupies one square on the board.
This version of the game has been built with the aim to be involved in a funny exercise to familiarize with Object Oriented Programming.

Users fight against the computer and, in order to win, need to find all of its battleships before it finds theirs.

![Responsiveness](/assets/media/responsiveness.png "Responsive Design")

<br>

[Live link to Battleship Challenge](https://maurizio-github.github.io/portfolio-project-2/)

<br>

## Table of Contents:

<br>

1. [How to play](#how-to-play)

2. [Features](#features)

3. [Data Model](#data-model)

4. [Testing](#testing)

5. [Validation](#validation)

6. [Bugs](#bugs)

7. [Deployment](#deployment)

8. [Credits](#credits)

<br>

## How to play

<br>

Battleship Challenge is based on the classic pen-and-paper game. More information about it can be found on [Wikipedia](https://en.wikipedia.org/wiki/Battleship_(game)).

In this version, players enter their name and two boards are randomly generated: one for each opponent. Players can see where their ships are, marked by a '■' sign, but obviously cannot see where the computer's ships are.

Guesses can resukt in a 'miss', which is indicated on the boards with an 'x', or in a 'hit', which is marked by a '#'. The player and the computer then take it in turns to make guesses and try to sink each other's battleships.

The winner is the one who sinks all of the opponent's battleships first.

<br>

[Back to Top](#table-of-contents)

<br>

## Features

<br>

- Random boards generation

    - Ships are randomly placed on both the player and computer boards (players cannot see where the computer's battleships are):
    ![Boards](/assets/media/boards-generation.png "Boards")

<br>

- Acceptance of user inputs, scores management and reset & restart option

    - In each turn, user inputs are properly processed. After any guess, a visual feedback is printed out to clearly show the current battle situation. A player can always leave and restart a new battle by pressing "r":
    ![Turn Management](/assets/media/turns-management.png "Turn Management")

<br>

- Input validation and error checking

    - Players can only enter integers for rows, cannot enter coordinates outside the board size and cannot enter the same guess more than once:
    ![Input Validation](/assets/media/inputs-validation.png "Input Validation")

<br>

[Back to Top](#table-of-contents)

<br>

## Data model

<br>

A Board-class has been built as the game data model. Two instances of this class are created to hold the player's and the computer's board.

The class stores the board size, the number of ships, the position of the ships, the guesses against that board, and other details such as the board owner (player or computer) and the player's name.

The class also has methods to help play the game, such as a method to print out the current board, a method to add ships to the board and a method to add a guess and return the result.

<br>

## Testing

<br>

This game has been tested by doing the following:

- Passed the code through a PEP8 linter and confirmed there are no problems;
- Given invalid inputs, such as strings where numbers are expected, out of bounds inputs, same inputs multiple times;
- Tested in a local terminal as well as the Code Institute Heroku terminal.

<br>

[Back to Top](#table-of-contents)

<br>

## Validation

<br>

- PEP8

    - No errors were returned by using 'pycodestyle'.

<br>

[Back to Top](#table-of-contents)

<br>

## Bugs

<br>

- Fixed bugs

    - There were some unexpected behaviours due to the absence, in a few parts of the code, of explicit call to the int() method to properly convert user inputs. Everything was fixed by troubleshooting and retested.

<br>

- Unfixed bugs

    - No bugs at this writing.

<br>

- Future developments

    - Having ships larger than 1x1 to properly reproduce the original game and, as a consequence, allowing players to position ships themselves and to select the board size (since, with 1x1 ships, a classic 10x10 grid would have been too dispersive at the moment).
    - An additional feature, as a necessary consequence of the previous point, is providing computer with intelligence, since with long ships, when it starts hitting, its next guess cannot be random; it must be contiguous.

<br>

[Back to Top](#table-of-contents)

<br>

## Deployment

<br>

- This project has been deployed using Code Institute's mock terminal for Heroku. Here are the steps followed for deployment:

    - Cloned this repository;
    - Created a new Heroku app;
    - Set the buildbacks to Python and NodeJS in that order;
    - Linked the Heroku app to the repository;
    - Clicked on **Deploy**.

<br>

The live link can be found here: [Battleship Challenge](https://maurizio-github.github.io/portfolio-project-2/).

<br>

[Back to Top](#table-of-contents)

<br>

## Credits

<br>

- Code Institute for the deployment terminal and a piece of code for setting the Board-class;
- Wikipedia for the details of the original Battleship game.

<br>

[Back to Top](#table-of-contents)