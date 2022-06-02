import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def dfs(i, j):
    v[i][j] = cnt
    dict[cnt] = dict.get(cnt, 0) + 1
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if not (0<=ni<N and 0<=nj<M) or arr[ni][nj] or v[ni][nj]:
            continue
        dfs(ni, nj)

N, M = map(int, input().split())

arr = [list(map(int, input().rstrip())) for _ in range(N)]
v = [[0 for _ in range(M)] for _ in range(N)]

dict = {}

cnt = 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and not v[i][j]:
            dfs(i, j)
            cnt += 1


for i in range(N):
    for j in range(M):
        result = 0
        if arr[i][j] == 1:
            result += 1
            check = []
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]
                if not (0<=ni<N and 0<=nj<M) or arr[ni][nj]:
                    continue
                if v[ni][nj] not in check:
                    check.append(v[ni][nj])
                    result += dict[v[ni][nj]]
        print(result%10, end='')
    print()