import numpy as np
from game import Agent, Board


class RandomAgent(Agent):
    def select_hole(self, board, pid):
        valid_holes = np.nonzero(board.board[pid, 0:6])[0]
        if len(valid_holes) == 0:
            return None
        return np.random.choice(valid_holes)


class QLearningAgent(Agent):
    def __init__(self):
        self._qtable = {}
        self._actions = range(6)


    def select_hole(self, board, pid):
        valid_holes = np.nonzero(board.board[pid, 0:6])[0]
        if len(valid_holes) == 0:
            return None
        return np.random.choice(valid_holes)
