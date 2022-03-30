import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    cnt = 1
    v[i][j] = True
    for d in range(4):
        ni = i + (di[d] * int(arr[i][j]))
        nj = j + (dj[d] * int(arr[i][j]))

        if not (0<=ni<N and 0<=nj<M) or arr[ni][nj] == 'H':
            continue
        
        if v[ni][nj]:
            print(-1)
            exit()

        cnt = max(cnt, dfs(ni, nj)+1)
    
    v[i][j] = False
    dp[i][j] = cnt
    return cnt



di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]
v = [[False for _ in range(M)] for _ in range(N)]
dp = [[-1 for _ in range(M)] for _ in range(N)]

print(dfs(0, 0))