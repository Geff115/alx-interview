#!/usr/bin/python3
"""
This script solves the N queens problem.
The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard
"""

import sys


def main():
    """
    Validates the input and calls the backtracking function.
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Now that N is valid, call the backtracker
    backtracker(N)


def backtracker(N: int):
    """
    Solves the N queens problem using backtracking.
    Prints all possible solutions.
    """
    # Set of columns where queens are placed
    columns = set()
    # Set of diagonals
    main_diag = set()
    anti_diag = set()
    board = [-1] * N

    def solve(row: int):
        if row == N:
            print_solution(board)
            return

        for col in range(N):
            # Check if placing queen is safe
            if col in columns or (row - col) in main_diag or \
              (row + col) in anti_diag:
                continue

            # Place queen
            board[row] = col
            columns.add(col)
            main_diag.add(row - col)
            anti_diag.add(row + col)

            # Recurse to place queens in next row
            solve(row + 1)

            # Backtrack: remove queen and undo attacks
            columns.remove(col)
            main_diag.remove(row - col)
            anti_diag.remove(row + col)

    def print_solution(board):
        """Print the board as a solution."""
        solution = [[row, board[row]] for row in range(N)]
        print(solution)

    # Start solving from the first row
    solve(0)


main()
