from collections import deque
import sys
N = int(sys.stdin.readline())
M = list(map(int, sys.stdin.readline().rstrip()))

stack = deque()
answer = [-1] * N
stack.append([0,0])
for i in range(N):
    while stack and M.count(stack[-1][0]) < M.count(M[i]):
        tep, idx = stack.pop()
        answer[idx] = M.count(M[i])
    stack.append([i,M[i]])
print(*answer)