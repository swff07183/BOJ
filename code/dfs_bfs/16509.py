import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

di = [
    [-1, -1, -1],
    [-1, -1, -1],
    [1, 1, 1],
    [1, 1, 1],
    [0, -1, -1],
    [0, 1, 1],
    [0, -1, -1],
    [0, 1, 1],
]
dj = [
    [0, -1, -1],
    [0, 1, 1],
    [0, -1, -1],
    [0, 1, 1],
    [-1, -1, -1],
    [-1, -1, -1],
    [1, 1, 1],
    [1, 1, 1],
]

def bfs():
    queue = deque()
    v = [[False for _ in range(M)] for _ in range(N)]
    v[r1][c1] = True
    queue.append([r1, c1])
    cnt = 0
    while queue:
        for _ in range(len(queue)):
            i, j = queue.popleft()
            if arr[i][j] == 1:
                return cnt
            for k in range(8):
                ni, nj = i, j
                flag = False
                for d in range(3):
                    ni += di[k][d]
                    nj += dj[k][d]
                    if not (0<=ni<N and 0<=nj<M) or (d != 2 and arr[ni][nj]):
                        flag = True
                        break
                if flag or v[ni][nj]:
                    continue
                v[ni][nj] = True
                queue.append([ni, nj])
        cnt += 1
    return -1
                

N = 10
M = 9
arr = [[0 for _ in range(M)] for _ in range(N)]

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())
arr[r2][c2] = 1

result = bfs()
print(result)