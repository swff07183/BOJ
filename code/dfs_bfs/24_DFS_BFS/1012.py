import sys
sys.setrecursionlimit(10000)

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(y, x):
    # print(x, y)
    for idx_d in range(4):
        ni = y + di[idx_d]
        nj = x + dj[idx_d]
        # 범위를 벗어났거나 이미 방문했다면 탐색 X
        if (not (0<=ni<N and 0<=nj<M)):
            continue
        if arr[ni][nj]==1 and visited[ni][nj]==0 :
            # 아니면 탐색 진행
            visited[ni][nj] = 1
            dfs(ni, nj)
    return


T = int(input())

for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    data = []
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1
        data.append([Y, X])

    cnt = 0
    for y, x in data:
        if visited[y][x] == 0:
            visited[y][x] = 1
            cnt += 1
            dfs(y, x)
    print(cnt)