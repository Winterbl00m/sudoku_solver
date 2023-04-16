import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

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


print(verify_board_dimensions(board))
display_board(board)