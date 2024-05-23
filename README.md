# Edwards Battleship

Edwards Battleship is a Python terminal game which runs in the Code Institute mock terminal on Heroku.

It is based on the classic Battleships board game where players have to try and guess the location of their opponents battleship(s). The aim is to 'sink' the opponents battleship. Each battleship occupies one square of the board.

![image](https://github.com/EdwardJWalsh/battleship/assets/155949281/565d5221-cfde-44da-b4cc-9348af326218)


## How To Play

* Player starts by entering thier name.
* Two boards are randomly generated (one for the player and one for the computer, which in this case is the opponent.
* The players ships location will be indicated by an 'S', Player will not be able to see the location of opponents ship.
* Player will then be prompted to enter a row and column on the board.
* Player and computer take turns to try to sink the others battleship.

## Features

* Name prompt
This asks the player for their name, this will be used throughout the game creating a more personalised gaming experience

![image](https://github.com/EdwardJWalsh/battleship/assets/155949281/bf3e7527-1871-419c-81bd-9c0bde3cfd10)

* Random board generation
Game randomly generates two boards on startup. The players ship is visible, the opponents is not

![image](https://github.com/EdwardJWalsh/battleship/assets/155949281/90e28e11-db45-47a3-9190-60621c9e6db2)

* Accepts users input
Returns message stating whether player or computer were successful

![image](https://github.com/EdwardJWalsh/battleship/assets/155949281/75121d41-1e70-4e51-8ae7-cff9bc1e6261)

Player recieves error message if data that is not a number is entered

![image](https://github.com/EdwardJWalsh/battleship/assets/155949281/384d658e-64b0-4fff-9d70-6d05be420b41)

Player recieves error message if co-ordinates are outside the range of the board

![image](https://github.com/EdwardJWalsh/battleship/assets/155949281/e4fde7e5-897f-4f56-a9fa-bbd95f73a78e)








