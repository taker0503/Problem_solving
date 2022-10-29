import sys
N = int(sys.stdin.readline())
for i in range(N):
    braket = str(sys.stdin.readline())[:-1]
    left = 0
    right = 0
    Answer= 'YES'
    for j in braket:
        if len(braket) % 2 != 0:
            Answer= 'NO'
            break
        if j =='(':
            left += 1
        else:
            right += 1
        if left < right:
            Answer= 'NO'
            break
    if left != right:
        Answer= 'NO'
    print(Answer)