from game import Game, Board
from agents import RandomAgent

if __name__ == "__main__":
    Game(Board(), RandomAgent(), RandomAgent()).run()
