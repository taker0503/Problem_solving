from collections import deque
N, M, K, X = map(int,input().split())
node = [[]for _ in range(N+1)]
count = [ -1 for _ in range(N+1)]
result = []
for i in range(M):
    A, B = map(int,input().split())
    node[A].append(B)

def solution():
    queue = deque([X])
    count[X] = 0
    while queue:
        x = queue.popleft()
        for i in node[x]:
            if count[i] == -1:
                count[i] = count[x] + 1
                if i not in queue:
                    queue.append(i)
    for i in range(N+1):
        if count[i] == K:
            result.append(i)

    return result if len(result) else -1



print(solution())