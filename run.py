# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from random import randint

# Define Board class to represent the board
class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['O'] * size for _ in range(size)]

    def print_board(self):
        for row in self.grid:
            print(" ".join(row))

# Define Ship class
class Ship:
    def __init__(self, row, col):
        self.row = row
        self.col = col

# Define Player class
class Player:
    def __init__(self, name):
        self.name = name
        self.board = None
        self.ships = []

def initialize_game(player_name):
    player = Player(player_name)
    player.board = Board(6)  # Assuming board size is 6x6
    return player

def place_ship(board, ship):
    # Logic to place the ship on the board
    pass

def print_boards(player_board, computer_board):
    print("Player's Board:")
    player_board.print_board()
    print("\nComputer's Board:")
    computer_board.print_board()  # Hide the computer's ships

def game_play(player):
    print("\nWelcome to Battleship!!!!\n")

    play_again = "YES"
    while play_again.lower() == "yes":
        size = 6
        computer_board = Board(size)

        # Place ships
        ship_row_player = randint(0, size - 1)
        ship_col_player = randint(0, size - 1)
        player.ships.append(Ship(ship_row_player, ship_col_player))

        ship_row_computer = randint(0, size - 1)
        ship_col_computer = randint(0, size - 1)
        # S for ship
        computer_board.grid[ship_row_computer][ship_col_computer] = 'S'

        for turn in range(4):
            print_boards(player.board, computer_board)
            print(f"\nTurn {turn + 1}")
            try:
                guess_row = int(input(f"{player.name}, guess row: "))
                guess_col = int(input(f"{player.name}, guess column: "))

                if (guess_row == ship_row_computer and
                        guess_col == ship_col_computer):
                    print(f"\nCongratulations, {player.name}! You sank the computer's battleship!\n")
                    break
                else:
                    if (guess_row not in range(size) or
                            guess_col not in range(size)):
                        print("\nOops, that’s not even in the ocean!\n")
                    elif computer_board.grid[guess_row][guess_col] == "X":
                        print("\nYou guessed that one already.\n")
                    else:
                        print("\nYou missed the computer's battleship!\n")
                        computer_board.grid[guess_row][guess_col] = "X"

                    # Computer's turn to guess
                    comp_guess_row = randint(0, size - 1)
                    comp_guess_col = randint(0, size - 1)

                    player_board = player.board.grid
                    comp_guess = player_board[comp_guess_row][comp_guess_col]
                    if comp_guess == "X":
                        print("\nThe computer guessed that one already.\n")
                    else:
                        print("\nThe computer missed your battleship!\n")
                        player_board[comp_guess_row][comp_guess_col] = "X"

                if turn == 3:
                    print("\nGAME OVER\n")
            except ValueError:
                print("\nPlease enter a valid number.\n")

        play_again = input(f"Do you want to play again, {player.name}? (Yes/No): ")

    print(f"\nTHANKS FOR PLAYING WITH US, {player.name.upper()}!!")

def main():
    player_name = input("Please enter your name: ")
    player = initialize_game(player_name)
    game_play(player)

main()