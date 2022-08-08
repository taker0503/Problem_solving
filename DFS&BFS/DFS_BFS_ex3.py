N, K = map(int,input().split())
graph = []
ex = [[0]*N for _ in range(N)]
dx = [1, 0 , -1, 0]
dy = [0, 1, 0, -1]
for _ in range(N):
    graph.append(list(map(int,input().split())))
s,x,y = map(int,input().split())

def solution():
    global s
    for i in range(N):
        for j in range(N):
            ex[i][j] = graph[i][j]
    while s > 0:
        s -= 1
        for i in range(N):
            for j in range(N):
                if graph[i][j] != 0:
                    k = ex[i][j]
                    virus(i,j,k)
    return ex[x-1][y-1]


def virus(i,j,k):
    k = min(ex[i][j],k)
    for idx in range(4):
        nx = i +dx[idx]
        ny = j +dy[idx]
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        if ex[nx][ny] == 0:
            ex[nx][ny] = k


print(solution())