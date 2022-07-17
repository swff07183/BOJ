"""
인구이동
"""
from collections import deque

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def move(si, sj):
    global cnt
    queue = deque()
    queue.append([si, sj])

    group = [[si, sj]]          # 연합 국가
    total = arr[si][sj]         # 연합의 인구 수 합
    visited[si][sj] = True
    while queue:
        i, j = queue.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if not (0<=ni<N and 0<=nj<N) or visited[ni][nj] or not (L <= abs(arr[i][j]-arr[ni][nj]) <= R):
                continue
            visited[ni][nj] = True
            group.append([ni, nj])
            queue.append([ni, nj])
            total += arr[ni][nj]
    if len(group) > 1:
        tmp = total // len(group)
        for i, j in group:
            arr[i][j] = tmp
        cnt += 1
    return


N, L, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0 

while True:
    cnt = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                move(i, j)
    if not cnt:
        break
    ans += 1
print(ans)
