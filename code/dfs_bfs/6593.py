import sys
from collections import deque
input = sys.stdin.readline

di = [-1, 1, 0, 0, 0, 0]
dj = [0, 0, -1, 1, 0, 0]
dk = [0, 0, 0, 0, -1, 1]

def bfs():
    v = [[[False for _ in range(C)] for _ in range(R)] for _ in range(L)]
    si, sj, sk = start 
    queue = deque()
    v[si][sj][sk] = True
    queue.append([si, sj, sk, 0])
    while queue:
        i, j, k, dis = queue.popleft()
        if arr[i][j][k] == "E":
            return f'Escaped in {dis} minute(s).'
        for d in range(6):
            ni = i + di[d]
            nj = j + dj[d]
            nk = k + dk[d]
            if not (0<=ni<L and 0<=nj<R and 0<=nk<C) or arr[ni][nj][nk] == '#' or v[ni][nj][nk]:
                continue
            v[ni][nj][nk] = True
            queue.append([ni, nj, nk, dis+1])
    return 'Trapped!'



while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0:
        break
    
    arr = []
    for _ in range(L):
        arr.append([list(input().rstrip()) for _ in range(R)])
        input()

    
    # 시작점 찾기
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if arr[i][j][k] == 'S':
                    start = (i, j, k)

    result = bfs()
    print(result)