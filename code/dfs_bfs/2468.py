import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(i, j):
    v[i][j] = True
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if not(0<=ni<N and 0<=nj<N) or v[ni][nj] or arr[ni][nj] <= height:
            continue
        dfs(ni, nj)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 1
max_height = 0
for i in range(N):
    for j in range(N):
        max_height = max(arr[i][j], max_height)
        
for height in range(1, max_height):
    v = [[False for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > height and not v[i][j]:
                dfs(i, j)
                cnt += 1
    result = max(result, cnt)

print(result)