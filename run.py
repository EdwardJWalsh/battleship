# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from random import randint

class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['O'] * size for _ in range(size)]

    def print_board(self):
        for row in self.grid:
            print(" ".join(row))

class Ship:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class Player:
    def __init__(self, name):
        self.name = name
        self.board = None
        self.ships = []

def initialize_game(player_name):
    player = Player(player_name)
    player.board = Board(6)  # Assuming board size is 6x6
    return player

def main():
    player_name = input("Please enter your name: ")
    player = initialize_game(player_name)
    game_play(player)

if __name__ == "__main__":
    main()