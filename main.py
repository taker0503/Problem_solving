N, M = map(int,input().split())
graph = []
ex = [[0] * M for _ in range(N)]
dx = [-1, 0 , 1, 0]
dy = [ 0 , 1, 0 , -1]
result = 0
for _ in range(M):
    graph.append(list(map(int,input().split())))

def solution(cnt):
    global result
    if cnt == 3:
        for i in range(M):
            for j in range(N):
                ex[i][j] = graph[i][j]
        for i in range(M):
            for j in range(N):
                if ex[i][j] == 2:
                    virus(i,j)
        result = max(result, get_score())
        return

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 0:
                graph[i][j] = 1
                cnt += 1
                solution(cnt)
                graph[i][j] = 0
                cnt -= 1
    return result


def get_score():
    count = 0
    for i in range(M):
        for j in range(N):
            if ex[i][j] == 0:
                count += 1
    return count

def virus(i,j):
    for idx in range(4):
        nx = i + dx[idx]
        ny = j + dy[idx]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if ex[nx][ny] == 0:
            ex[nx][ny] = 2
            virus(nx,ny)

print(solution(0))