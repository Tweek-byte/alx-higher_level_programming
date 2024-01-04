#!/usr/bin/python3
"""
N-Queens backtracking program to print the coordinates of N queens
on an NxN grid such that they are all in non-attacking positions.
"""

from sys import argv

if __name__ == "__main__":
    chessboard = []
    
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    
    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)
    
    board_size = int(argv[1])
    
    if board_size < 4:
        print("N must be at least 4")
        exit(1)

    # Initialize the chessboard
    for i in range(board_size):
        chessboard.append([i, None])

    def queen_already_exists(y):
        """Check that a queen does not already exist in that y value."""
        for x in range(board_size):
            if y == chessboard[x][1]:
                return True
        return False

    def reject_solution(x, y):
        """Determines whether or not to reject the solution."""
        if queen_already_exists(y):
            return False
        i = 0
        while i < x:
            if abs(chessboard[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_chessboard(x):
        """Clears the chessboard from the point of failure on."""
        for i in range(x, board_size):
            chessboard[i][1] = None

    def solve_nqueens(x):
        """Recursive backtracking function to find the solution."""
        for y in range(board_size):
            clear_chessboard(x)
            if reject_solution(x, y):
                chessboard[x][1] = y
                if x == board_size - 1:
                    print(chessboard)
                else:
                    solve_nqueens(x + 1)  # Move on to the next x value to continue

    # Start the recursive process at x = 0
    solve_nqueens(0)
