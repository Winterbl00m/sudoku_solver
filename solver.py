import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from numpy.lib.stride_tricks import as_strided

def display_board(board):
    # Create a colored grid with Matplotlib
    fig, ax = plt.subplots(figsize=(5, 5))

    # Add grid lines to the plot
    ax.grid(which='major', color='grey', linewidth=1)

    # Set the ticks and labels for the x and y axes
    ax.set_xticks(np.arange(-0.5, 9.5, 1))
    ax.set_yticks(np.arange(-0.5, 9.5, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    for i in range(3):
        ax.axhline(3* i - .5, color='grey', linewidth=4)
        ax.axvline(3 * i - .5, color='grey', linewidth=4)

    # Add the numbers to the plot
    for i in range(9):
        for j in range(9):
            if board[i, j] != 0:
                ax.text(j, i, str(board[i, j]), fontsize=20, 
                        ha='center', va='center', color='black')

    # Show the plot
    plt.show()

def verify_board_dimensions(board):
    height, width = board.shape
    if height != width: 
        print("board is not square")
        return False
    elif not math.sqrt(height).is_integer():
        print("board is not a square")
        return False
    else:
        return True

def extract_squares(board):
    square_size = int(sqrt(sqrt(board.size)))

    # create an example array
    arr = board.copy()

    # split the array into sub-grids
    squares = arr.reshape((square_size, square_size, square_size, square_size)).transpose((0, 2, 1, 3)).reshape((square_size ** 2, square_size, square_size))

    return(squares)

def nums_not_in(shape):
    n = shape.size
    nums_not_in = {i + 1 for i in range(n) if i + 1 not in shape}
    return nums_not_in


def makes_notes(board):
    width, height = board.shape
    notes = [[{} for row in range(width)] for col in range(height)]
    squares = extract_squares(board)
    ys, xs = np.where(board == 0)
    for i in range(len(xs)):
        x = xs[i]
        y = ys[i]
        square_num = x // 3 + 3 * (y // 3)
        square = squares[square_num]
        nums_not_in_square = nums_not_in(square)
        nums_not_in_row = nums_not_in(board[y])
        nums_not_in_col = nums_not_in(board.transpose()[x])
        possible_nums = nums_not_in_square.intersection(nums_not_in_row, nums_not_in_col)
        notes[x][y] = possible_nums
    return np.array(notes)
    

# def fill_board(board, notes):
#     if len(possible_nums) == 1:
#         board[x][y] = list(possible_nums)[0]


# Create a sample Sudoku as a 9x9 NumPy array
data = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]]
board = np.array(data)
print(board)

notes = makes_notes(board)
print(notes)

squares = extract_squares(notes)
print(squares)


