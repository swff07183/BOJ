import sys
sys.stdin = open('input.txt')

from collections import deque

# 상 하 좌 우 앞 뒤
di = [-1, 1, 0, 0, 0, 0]
dj = [0, 0, -1, 1, 0, 0]
dk = [0, 0, 0, 0, -1, 1]

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H) ]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]

queue = deque()
total = N * M * H
tomato = 0
day = 0

for i in range(N):
    for j in range(M):
        for k in range(H):
            if arr[k][i][j] == 1:
                queue.append((i, j, k))
                visited[k][i][j] = 1
                tomato += 1
            elif arr[k][i][j] == -1:
                total -= 1

while total > tomato:
    count = 0
    for _ in range(len(queue)):
        i, j, k = queue.popleft()
        for idx_d in range(6):
            ni = i + di[idx_d]
            nj = j + dj[idx_d]
            nk = k + dk[idx_d]
            if (0<=ni<N and 0<=nj<M and 0<=nk<H) and visited[nk][ni][nj] == 0 and arr[nk][ni][nj] != -1:
                queue.append((ni, nj, nk))
                visited[nk][ni][nj] = visited[k][i][j] + 1
                tomato += 1
                count += 1
    if count == 0:
        # 더이상 바뀔 토마토가 없을 때
        day = -1
        break
    day += 1

print(day)