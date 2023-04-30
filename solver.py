import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from numpy.lib.stride_tricks import as_strided

def display_board(board):
    num_symbols = int(sqrt(board.size))
    square_size = int(sqrt(num_symbols))

    # Create a colored grid with Matplotlib
    fig, ax = plt.subplots(figsize=(5, 5))

    # Add grid lines to the plot
    ax.grid(which='major', color='grey', linewidth=1)

    # Set the ticks and labels for the x and y axes

    ax.set_xticks(np.arange(-0.5, num_symbols + 0.5, 1))
    ax.set_yticks(np.arange(-0.5, num_symbols + 0.5, 1))
    ax.set_xticklabels([])
    ax.set_yticklabels([])

    for i in range(square_size):
        ax.axhline(square_size * i - .5, color='grey', linewidth=4)
        ax.axvline(square_size * i - .5, color='grey', linewidth=4)

    # Add the numbers to the plot
    for i in range(num_symbols):
        for j in range(num_symbols):
            if board[i, j] != 0 and board[i,j] != "0":
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

def extract_square(board, pos):
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False


def nums_in(shape):
    n = shape.size
    nums_in = {i + 1 for i in range(n) if i + 1 in shape}
    return nums_in


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

def valid(board, num, pos):
    x,y = pos
    row = board[x]
    col = board.transpose()[y]

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    if num in nums_in(row):
        return False
    if num in nums_in(col):
        return False

    return True


def find_empty(board):
    if np.isin(0, board):
        indices = np.where(board == 0)
        i = indices[0][0]
        j = indices[1][0]
        return i,j    
    else:
        return None


def solve(board):
    find = find_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


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
solve(board)
print(board)
