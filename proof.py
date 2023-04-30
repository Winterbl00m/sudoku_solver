from solver import display_board
import numpy as np

data = [[0, 0, 0, 0],
        [3, 0, 0, 0],
        [0, 4, 0, 0],
        [0, 0, 3, 0]]
board = np.array(data)
display_board(board)