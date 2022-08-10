from itertools import combinations

N = int(input())

board = []
teacher = []
spaces = []

for i in range(N):
    board.append(list(input().split()))
    for j in range(N):
        if board[i][j] == 'T':
            teacher.append((i,j))
        if board[i][j] == 'X':
            spaces.append((i,j))

def check_std(i,j,state):

    if state == 0:
        while i >= 0:
            if board[i][j] == 'S':
                return True
            if board[i][j] == 'O':
                return False
            i -= 1

    elif state == 1:
        while j < N:
            if board[i][j] == 'S':
                return True
            if board[i][j] == 'O':
                return False
            j += 1
    if state == 2:
        while i < N:
            if board[i][j] == 'S':
                return True
            if board[i][j] == 'O':
                return False
            i += 1
    if state == 3:
        while j >= 0:
            if board[i][j] == 'S':
                return True
            if board[i][j] == 'O':
                return False
            j -= 1
    return False


def solution():
    for x, y in teacher:
        for i in range(4):
            if check_std(x,y,i):
                return True
    return False

find = False

for data in combinations(spaces,3):
    for x,y in data:
        board[x][y] = 'O'
    if not solution():
        find = True
        break
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')


