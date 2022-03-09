import sys
sys.setrecursionlimit(10000)

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(i, j, count):
    # print(x, y)
    for idx_d in range(4):
        ni = i + di[idx_d]
        nj = j + dj[idx_d]
        # 범위를 벗어났거나 이미 방문했다면 탐색 X
        if (not (0<=ni<N and 0<=nj<N)):
            continue
        if arr[ni][nj] == 1 and visited[ni][nj] == 0 :
            # 아니면 탐색 진행
            visited[ni][nj] = 1
            count = dfs(ni, nj, count+1)
    return count


N = int(input())
arr = [list(map(int, list(input()))) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]
result = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and visited[i][j] == 0:
            visited[i][j] = 1
            result.append(dfs(i, j, 1))
result.sort()
print(len(result))
for n in result:
    print(n)