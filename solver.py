import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from numpy.lib.stride_tricks import as_strided

class Board():
    def __init__(self, data):
        self.n = len(data)
        if not sqrt(self.n).is_integer():
            raise ValueError("data must be a square size (i.e 4,9, 16, 25...).")
        self.box_size = int(sqrt(self.n))
        self.board = np.array(data)
        height, width = self.board.shape
        if height != width:
            raise ValueError("data's height is not equal to its width.")

    def display(self):
        # Create a colored grid with Matplotlib
        fig, ax = plt.subplots(figsize=(5, 5))

        # Add grid lines to the plot
        ax.grid(which='major', color='grey', linewidth=1)

        # Set the ticks and labels for the x and y axes

        ax.set_xticks(np.arange(-0.5, self.n + 0.5, 1))
        ax.set_yticks(np.arange(-0.5, self.n + 0.5, 1))
        ax.set_xticklabels([])
        ax.set_yticklabels([])

        for i in range(self.box_size):
            ax.axhline(self.box_size * i - .5, color='grey', linewidth=4)
            ax.axvline(self.box_size * i - .5, color='grey', linewidth=4)

        # Add the numbers to the plot
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i, j] != 0 and self.board[i,j] != "0":
                    ax.text(j, i, str(self.board[i, j]), fontsize=20, 
                            ha='center', va='center', color='black')

        # Show the plot
        plt.show()

    def valid(self, num, pos):
        x,y = pos
        row = self.board[x]
        col = self.board.transpose()[y]

        #Check row 
        if num in row:
            return False

        #Check column
        if num in col:
            return False

        # Check box
        box_x = pos[1] // self.box_size
        box_y = pos[0] // self.box_size
        for i in range(box_y*self.box_size, box_y*self.box_size + self.box_size):
            for j in range(box_x*self.box_size, box_x*self.box_size + self.box_size):
                if self.board[i][j] == num and (i,j) != pos:
                    return False

        return True


    def find_empty(self):
        if np.isin(0, self.board):
            indices = np.where(self.board == 0)
            i = indices[0][0]
            j = indices[1][0]
            return i,j    
        else:
            return None


    def solve(self):
        find = self.find_empty()
        if not find:
            return True
        else:
            row, col = find

        for num in range(1,self.n + 1):
            if self.valid(num, (row, col)):
                self.board[row][col] = num

                if self.solve():
                    return True

                self.board[row][col] = 0

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

board = Board(data)
board.solve()
board.display()
