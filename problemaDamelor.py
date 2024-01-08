from itertools import permutations

def is_solution(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                return False
    return True

def place_queens():
    for perm in permutations(range(8)):
        board = [[0] * 8 for _ in range(8)]

        for row, col in enumerate(perm):
            board[row][col] = 1
            # Mark horizontal and vertical
            for i in range(8):
                board[row][i] = 1
                board[i][col] = 1
            # Mark diagonals
            for i in range(8):
                for j in range(8):
                    if abs(row - i) == abs(col - j):
                        board[i][j] = 1

        if is_solution(board):
            return perm
    return None

solution = place_queens()
solution
print(solution)