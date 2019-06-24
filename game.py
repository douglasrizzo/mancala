import numpy as np
import logging


class Board():
    def __init__(self, log=True):
        # whereas real mancala, which is played counter-clockwise, may be represented like this:
        # 0 4 4 4 4 4 4
        #   4 4 4 4 4 4 0
        # here we simplify things and just go back to the beginning
        # 4 4 4 4 4 4 0
        # 4 4 4 4 4 4 0
        self._board = np.array([[4] * 6 + [0], [4] * 6 + [0]])
        logging_level = logging.DEBUG if log else logging.CRITICAL
        logging.basicConfig(
            level=logging_level,
            filename='mancala.log',
            filemode='w',
            format='%(levelname)s - %(message)s')

    def __str__(self):
        value = str(self._board).replace('[', '').replace(']', '').strip()

        while '\n ' in value:
            value = value.replace('\n ', '\n')

        while '  ' in value:
            value = value.replace('  ', ' ')
        return value

    @property
    def board(self):
        return self._board

    def valid_initial_hole(self, pid):
        valid_holes = np.nonzero(self._board[pid, 0:6])[0]
        return len(valid_holes) != 0

    def play(self, pid, row, hole):
        logging.info('It\'s player\'s {0} turn!'.format(pid))

        # get the number of stones from the selected hole
        stones = self._board[row, hole]
        self._board[row, hole] = 0

        logging.info(
            'Player {0} selected hole ({1}, {2}), which has {3} stones!'.
            format(pid, row, hole, stones))

        next_hole = (row, hole)

        # let's start distributing the stones
        while stones > 0:
            # ignore the opponent's point hole
            if next_hole[1] == 5 and next_hole[0] != pid:
                next_hole = (int(not next_hole[0]), 0)
            elif next_hole[1] == 6 and next_hole[0] == pid:
                next_hole = (int(not next_hole[0]), 0)
            else:
                next_hole = (next_hole[0], next_hole[1] + 1)

            # add the actual stone
            self._board[next_hole] += 1
            stones -= 1

            logging.info('\n{0}'.format(self))

        if not self.valid_initial_hole(pid):
            exit
        elif next_hole[1] == 6 and next_hole[0] == pid:
            hole = np.random.choice(np.nonzero(self._board[pid, 0:6])[0])
            self.play(pid, pid, hole)
        elif self._board[next_hole] > 1:
            self.play(pid, next_hole[0], next_hole[1])


class Agent:
    def select_hole(self, board: Board, pid: int):
        pass


class Game():
    def __init__(self, board: Board, player1: Agent, player2: Agent):
        self._board = board
        self._player1 = player1
        self._player2 = player2

    def run(self):
        pid = np.random.choice([0, 1])

        while not self.over():
            current_player = self._player1 if pid == 0 else self._player2
            hole = current_player.select_hole(self._board, pid)
            self._board.play(pid, pid, hole)
            pid = int(not pid)

    def over(self):
        return not self._board.valid_initial_hole(
            0) or not self._board.valid_initial_hole(1)
