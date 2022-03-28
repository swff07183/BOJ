import sys
sys.stdin = open("input.txt")

from collections import deque

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 1
    while len(queue):
        i, j = queue.popleft()
        for idx_d in range(4):
            ni = i + di[idx_d]
            nj = j + dj[idx_d]
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                queue.append((ni, nj))
                visited[ni][nj] = visited[i][j]+1
                if (ni, nj) == (N - 1, M - 1):
                    return

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]


bfs()
print(visited[N-1][M-1])
