# Battleship Challenge!

This is a very simple website, built to engage users with an enjoyable pastime: 'Rock, Paper, Scissors, Lizard, Spock?', the game invented by Sam Kass in 1998 that recently became super popular thanks to 'The Big Bang Theory' TV series!

The site mainly targets people who typically are casual or regular pastime-consumers, like the ones who enjoy spending a few hours a week with solitaires and other similar games.

![Responsiveness](/assets/media/responsiveness.png "Responsive Design")

<br>

[Live link to Rock, Paper, Scissors, Lizard, Spock?](https://maurizio-github.github.io/portfolio-project-2/)

<br>

## Table of Contents:

<br>

1. [Features](#features)

2. [Testing](#testing)

3. [Validation](#validation)

4. [Bugs](#bugs)

5. [Deployment](#deployment)

6. [Credits](#credits)

<br>

## Features

<br>

- Simple header with a call to action

    - It welcomes the players with a neat sentence, immediately inviting them to act on the buttons (with visual feedback on hover) below it in order to start a new game:
    ![Buttons](/assets/media/buttons.png "Buttons")

<br>

- Game area with scores and feedback messages

    - Before a new game starts, this area provides players with a nice couple of pictures depicting the game rules. They just differ in their colours, in relation to player-side and computer-side respectively:
    ![Game Rules](/assets/media/images-area.png "Game Rules")
    - Once the game is running, pictures change to reflect player and computer choices, scores get updated based on game rules, moves left decrement accordingly and a feedback message appears to the bottom to clearly state who scored (i.e. who won):
    ![Game Area](/assets/media/game-area.png "Game Area")
    - After the 9 regular moves - if you got there - as it always depends on the total scores made during the game (whose winner must score 5 out of 9), in case of a draw (of course, regardless that the very last move ends up with a "Draw!", as in the case depicted below, or not), a tie-break phase starts. Just next to the counter saying that there are no moves left, a very clear feedback message warns about that:
    ![Tie-Break](/assets/media/tie-break.png "Tie-Break")
    - Tie-break phase goes on, possibly going through other draws, until one of the opponents scores and the game over condition is met. When this finally happens, one last message clearly stating who won the game is shown. The moves-buttons disappear and a restart button pops up (also this one with feedback on hover) to invite players to enter a new game:
    ![Game Over](/assets/media/game-over.png "Game Over")

<br>

[Back to Top](#table-of-contents)

<br>

## Testing

<br>

- The website was successfully tested on different browsers: Chrome, Edge, Safari.
- The website is responsive and looks good on different devices. Its functioning was successfully tested on all standard screen sizes by using Chrome DevTools as well as [Am I Responsive?](https://ui.dev/amiresponsive)
- I confirmed that any single piece of text is readable, easy to understand and fully accessible.
- I confirmed that the whole Javascript logic addressing the game rules and every possible outcome properly works.

<br>

[Back to Top](#table-of-contents)

<br>

## Validation

<br>

- HTML

    - No errors found via the official [W3C validator](https://validator.w3.org/#validate_by_input).

<br>

- CSS

    - No errors found via the official [Jigsaw validator](https://jigsaw.w3.org/css-validator/#validate_by_input).

<br>

- Javascript

    - No errors found via [JSHint](https://jshint.com/).

<br>

- Accessibility

    - I confirmed that both colors and fonts chosen are easy to read and tested accessibility via Lighthouse, within Chrome DevTools:
    ![Lighthouse](/assets/media/performance-lighthouse.png "Performance Analysis")

<br>

[Back to Top](#table-of-contents)

<br>

## Bugs

<br>

- Fixed bugs

    - There were some logic issues in properly handling the tie-break phase. Everything was fixed and retest after reviewing a few lines of JS code. Relevant comments have also been added to the code for reference.

<br>

- Unfixed bugs

    - No bugs at this writing.

<br>

- Future developments

    - Since it is just a simple game, with no need to capture user choices, any impression of 'overengineering' has been averted. Yet, it could still make sense to move the comparison logic used within the checkWinner() function to a data structure, i.e. an array of dictionaries, with each element representing everything we need to know about a specific move against any others.

<br>

[Back to Top](#table-of-contents)

<br>

## Deployment

<br>

- The website was deployed to GitHub Pages through the following steps:

    - Navigation to the 'Setting' tab within the project repository;
    - Selection of 'main' branch from the 'Branch' section dropdown menu;
    - Confirmation by clicking on 'Save' to get the link to the website.

<br>

The live link can be found here: [Rock, Paper, Scissors, Lizard, Spock?](https://maurizio-github.github.io/portfolio-project-2/).

<br>

[Back to Top](#table-of-contents)

<br>

## Credits

<br>

- Content

    - Ready-to-use code, making the very first part of the project, was taken and **properly adapted** from Coding Institute's [Love Maths](https://github.com/Code-Institute-Org/love-maths) project.

<br>

- Media

    - Every image presented was taken from [ClipArtMax](https://www.clipartmax.com/), apart from the pictures representing the game rules, which were taken from the web.

<br>

[Back to Top](#table-of-contents)