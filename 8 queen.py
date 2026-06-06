def solve(col=0):
    if col == 8:
        for r in board:
            print(*["Q" if x else "." for x in r])
        return True

    for row in range(8):
        if all(board[row][i] == 0 for i in range(col)) and \
           all(board[row-i][col-i] == 0 for i in range(1, min(row, col)+1)) and \
           all(board[row+i][col-i] == 0 for i in range(1, min(7-row, col)+1)):

            board[row][col] = 1

            if solve(col + 1):
                return True

            board[row][col] = 0

    return False

board = [[0]*8 for _ in range(8)]
solve()