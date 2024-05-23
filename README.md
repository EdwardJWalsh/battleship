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

Player receives error message if data that is not a number is entered

![image](https://github.com/EdwardJWalsh/battleship/assets/155949281/384d658e-64b0-4fff-9d70-6d05be420b41)

Player receives error message if co-ordinates are outside the range of the board

![image](https://github.com/EdwardJWalsh/battleship/assets/155949281/e4fde7e5-897f-4f56-a9fa-bbd95f73a78e)

## Data Model

__Board Class:__

Attributes:
* size: Size of the board (assumed to be a square grid).
* grid: 2D list representing the board with cells initialized to 'O' (ocean).

Methods:
* print_board(hide_ships=False): Prints the current state of the board.

__Ship Class__

Attributes:
* row: Row position of the ship.
* col: Column position of the ship.

__Player Class__

Attributes:
* name: Name of the player.
* board: Instance of the Board class representing the player's game board.
* ships: List containing instances of the Ship class representing the player's ships.

__Functions:__

* initialize_game(player_name): Initializes the game by creating a player instance and setting up the player's game board.
* place_ship(board, ship): Places a ship on the specified board.
* print_boards(player_board, computer_board): Prints both the player's and computer's game boards.
* game_play(player): Function to manage the gameplay, including turns, ship placement, and input handling.
* main(): Entry point of the program, prompts the user to enter their name, initializes the game, and starts gameplay.

__Dependencies__

The code does not rely on any external dependencies and can be run using Pythons built in libraries.






