import sys
from collections import deque
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
answer = [-1] * N
stack = deque()

for idx in range(N):
    while stack and stack[-1][0] < A[idx]:
        tmp, idx_ = stack.pop()
        answer[idx_] = A[idx]
    stack.append([A[idx], idx])
        
            
print(*answer)