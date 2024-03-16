
from collections import deque
import copy

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]


def infection():
    q = deque()
    arr = copy.deepcopy(data)
    virus_pos = check_virus()
    for pos in virus_pos:
        q.append(pos)

    visited = [[0 for _ in range(M)] for _ in range(N)]

    while len(q):
        i, j = q.popleft()
        if not visited[i][j]:
            visited[i][j] = 1
            for idx_d in range(4):
                ni = i + di[idx_d]
                nj = j + dj[idx_d]
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                    arr[ni][nj] = 2
                    q.append((ni, nj))

    return arr

def make_wall(cnt):
    global max_cnt
    if cnt == 3:
        arr = infection()
        safe_zones = check_safe_zone(arr)
        if safe_zones > max_cnt:

            max_cnt = safe_zones
        return
    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                data[i][j] = 1
                make_wall(cnt+1)
                data[i][j] = 0

def check_safe_zone(arr):
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                count += 1
    return count


def check_virus():
    result = []
    for i in range(N):
        for j in range(M):
            if data[i][j] == 2:
                result.append((i, j))

    return result

N, M = map(int, input().split())

data = [list(map(int, input().split())) for _ in range(N)]

max_cnt = 0

make_wall(0)
print(max_cnt)