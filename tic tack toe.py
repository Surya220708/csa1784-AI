board = [' ']*9

def show():
    print()
    print(board[0], '|', board[1], '|', board[2])
    print('--+---+--')
    print(board[3], '|', board[4], '|', board[5])
    print('--+---+--')
    print(board[6], '|', board[7], '|', board[8])
    print()

def win(p):
    w = [(0,1,2),(3,4,5),(6,7,8),
         (0,3,6),(1,4,7),(2,5,8),
         (0,4,8),(2,4,6)]
    return any(board[a]==board[b]==board[c]==p for a,b,c in w)

player = 'X'

for _ in range(9):
    show()
    pos = int(input(f"Player {player} (1-9): ")) - 1

    if board[pos] == ' ':
        board[pos] = player

        if win(player):
            show()
            print("Player", player, "Wins!")
            break

        player = 'O' if player == 'X' else 'X'
else:
    show()
    print("Draw!")