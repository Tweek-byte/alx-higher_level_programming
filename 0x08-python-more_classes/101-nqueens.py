from sys import argv

def initialize_board(size):
    """Initialize the chessboard with queens in non-attacking positions."""
    return [[i, None] for i in range(size)]

def already_exists(board, y):
    """Check that a queen does not already exist in that y value."""
    return any(y == queen[1] for queen in board)

def reject(board, x, y):
    """Determine whether or not to reject the solution."""
    if already_exists(board, y):
        return False
    return all(abs(queen[1] - y) != abs(i - x) for i, queen in enumerate(board[:x]))

def clear_board(board, start_index):
    """Clear the board from the point of failure on."""
    for i in range(start_index, len(board)):
        board[i][1] = None

def nqueens(board, x):
    """Recursive backtracking function to find the solution."""
    size = len(board)
    for y in range(size):
        clear_board(board, x)
        if reject(board, x, y):
            board[x][1] = y
            if x == size - 1:
                print([(queen[0], queen[1]) for queen in board])  # Print coordinates
            else:
                nqueens(board, x + 1)  # Move on to the next x value to continue

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)

    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # Initialize the chessboard
    chessboard = initialize_board(n)

    # Start the recursive process at x = 0
    nqueens(chessboard, 0)
