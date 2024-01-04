from sys import argv

def initialize_board(board_size):
    return [[i, None] for i in range(board_size)]

def queen_already_exists(board, y):
    return any(y == queen[1] for queen in board)

def reject_solution(board, x, y):
    if queen_already_exists(board, y):
        return False
    return all(abs(queen[1] - y) != abs(i - x) for i, queen in enumerate(board[:x]))

def clear_board(board, start_index):
    for i in range(start_index, len(board)):
        board[i][1] = None

def solve_nqueens(board, x):
    size = len(board)
    for y in range(size):
        clear_board(board, x)
        if reject_solution(board, x, y):
            board[x][1] = y
            if x == size - 1:
                print([(queen[0], queen[1]) for queen in board])
            else:
                solve_nqueens(board, x + 1)

if __name__ == "__main__":
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

    chessboard = initialize_board(board_size)
    solve_nqueens(chessboard, 0)
