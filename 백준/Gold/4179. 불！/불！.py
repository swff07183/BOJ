import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def in_range(i, j):
    return 0<=i<N and 0<=j<M

def bfs(si, sj):
    queue = deque()
    queue.append((si, sj))
    v = [[False for _ in range(M)] for _ in range(N)]
    v[si][sj] = True
    t = 0

    while queue:
        fire()
        t += 1
        for _ in range(len(queue)):
            i, j = queue.popleft()
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if not in_range(ni, nj):
                    return t
                if v[ni][nj] or arr[ni][nj] in ('#', 'F'):
                    continue
                queue.append([ni, nj])
                v[ni][nj] = True
    
    return "IMPOSSIBLE"

def fire():
    for _ in range(len(fires)):
        i, j = fires.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if not in_range(ni, nj) or arr[ni][nj] in ('F', '#'):
                continue
            arr[ni][nj] = 'F'
            fires.append((ni, nj))
            
    

N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]
fires = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'J':
            arr[i][j] = '.'
            si, sj = i, j
        elif arr[i][j] == 'F':
            fires.append((i, j))

ans = bfs(si, sj)
print(ans)

