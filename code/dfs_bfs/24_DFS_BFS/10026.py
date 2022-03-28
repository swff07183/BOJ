from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(si, sj, visited):
    queue = deque()
    color = arr[si][sj]
    queue.append((si, sj))
    visited[si][sj] = True
    while queue:
        i, j = queue.popleft()
        for idx_d in range(4):
            ni = i + di[idx_d]
            nj = j + dj[idx_d]
            if 0<=ni<N and 0<=nj<N and not visited[ni][nj]:
                if arr[ni][nj] == color:
                    visited[ni][nj] = True
                    queue.append((ni, nj))


def bfs_rg(si, sj, visited_rg):
    queue = deque()
    color = arr[si][sj]
    queue.append((si, sj))
    visited_rg[si][sj] = True
    while queue:
        i, j = queue.popleft()
        for idx_d in range(4):
            ni = i + di[idx_d]
            nj = j + dj[idx_d]
            if 0<=ni<N and 0<=nj<N and not visited_rg[ni][nj]:
                if (arr[ni][nj] == 'R' or arr[ni][nj] == 'G') and (color == 'R' or color == 'G'):
                    visited_rg[ni][nj] = True
                    queue.append((ni, nj))
                elif arr[ni][nj] == color:
                    visited_rg[ni][nj] = True
                    queue.append((ni, nj))



def section():
    cnt = 0
    section_cnt = 0
    section_rg_cnt = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited_rg = [[False for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                bfs(i, j, visited)
                section_cnt += 1
            if not visited_rg[i][j]:
                bfs_rg(i, j, visited_rg)
                section_rg_cnt += 1
    return (section_cnt, section_rg_cnt)


N = int(input())

arr = [list(input()) for _ in range(N)]
result = section()
print(*result)