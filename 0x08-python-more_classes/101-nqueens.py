from sys import argv

def initialize_chessboard(size):
    return [[i, None] for i in range(size)]

def already_exists(chessboard, y):
    return any(y == queen[1] for queen in chessboard)

def reject_solution(chessboard, x, y):
    if already_exists(chessboard, y):
        return False
    return all(abs(queen[1] - y) != abs(i - x) for i, queen in enumerate(chessboard[:x]))

def clear_chessboard(chessboard, start_index):
    for i in range(start_index, len(chessboard)):
        chessboard[i][1] = None

def nqueens(chessboard, x):
    size = len(chessboard)
    for y in range(size):
        clear_chessboard(chessboard, x)
        if reject_solution(chessboard, x, y):
            chessboard[x][1] = y
            if x == size - 1:
                print([(queen[0], queen[1]) for queen in chessboard])
            else:
                nqueens(chessboard, x + 1)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)

    size = int(argv[1])
    if size < 4:
        print("N must be at least 4")
        exit(1)

    chessboard = initialize_chessboard(size)
    nqueens(chessboard, 0)
