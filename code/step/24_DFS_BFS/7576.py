from collections import deque

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

queue = deque()
total = N*M
tomato = 0
day = 0

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append((i, j))
            visited[i][j] = 1
            tomato += 1
        elif arr[i][j] == -1:
            total -= 1

while total > tomato:
    count = 0
    for _ in range(len(queue)):
        i, j = queue.popleft()
        for idx_d in range(4):
            ni = i + di[idx_d]
            nj = j + dj[idx_d]
            if (0<=ni<N and 0<=nj<M) and visited[ni][nj] == 0 and arr[ni][nj] != -1:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
                tomato += 1
                count += 1
    if count == 0:
        # 더이상 바뀔 토마토가 없을 때
        day = -1
        break
    day += 1

print(day)