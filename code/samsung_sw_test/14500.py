import sys
sys.stdin = open("input.txt")

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def tetromino(cnt, total, i, j):
    global max_sum
    if cnt == 4:
        if max_sum < total:
            max_sum = total
        return
    for idx_d in range(4):
        ni = i + di[idx_d]
        nj = j + dj[idx_d]
        if (0<=ni<N and 0<=nj<M) and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            tetromino(cnt+1, total+arr[ni][nj], ni, nj)
            visited[ni][nj] = 0
        else:
            continue

def tetromino_t(i, j):
    global max_sum

    for ex_d in range(4):
        count = 1
        total = arr[i][j]
        for idx_d in range(4):
            if idx_d == ex_d:
                continue
            ni = i + di[idx_d]
            nj = j + dj[idx_d]
            if (0 <= ni < N and 0 <= nj < M):
                count += 1
                total += arr[ni][nj]
        if count == 4:
            if max_sum < total:
                max_sum = total




N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
max_sum = 0

for i in range(N):
    for j in range(M):
        tetromino(0, 0, i, j)
        tetromino_t(i, j)
print(max_sum)