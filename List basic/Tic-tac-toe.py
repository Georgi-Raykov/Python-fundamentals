board = []
winner = 'Draw!'
for _ in range(3):

    line = input()
    row = list(map(int, line.split()))
    board.append(row)

for i in range(3):

    if board[i][0] == board[i][1] == board[i][2] != 0:

        if board[i][0] == 1:
            winner = 'First player win'
        elif board[i][0] == 2:
            winner = 'Second player win'

    if board[0][i] == board[1][i] == board[2][i] != 0:

        if board[0][i] == 1:
            winner = 'First player win'
        elif board[0][i] == 2:
            winner = 'Second player win'
if board[0][0] == board[1][1] == board[2][2] != 0:

    if board[0][0] == 1:

        winner = 'First player win'
    elif board[0][0] == 2:
        winner = 'Second player win'

if board[0][2] == board[1][1] == board[2][0] != 0:

    if board[0][2] == 1:

        winner = 'First player win'
    elif board[0][2] == 2:
        winner = 'Second player win'

print(winner)