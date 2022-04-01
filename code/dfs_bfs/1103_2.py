import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(i, j, cnt):
    global result
    ret = cnt
    for d in range(4):
        ni = i + ((di[d]) * int(arr[i][j]))
        nj = j + (dj[d] * int(arr[i][j]))
        if not (0<=ni<N and 0<=nj<M) or dp[ni][nj] >= cnt+1 or arr[ni][nj]=='H':
            continue
        if v[ni][nj]:
            print(-1)
            exit()
        v[ni][nj] = True
        dp[ni][nj] = cnt+1
        dfs(ni, nj, cnt+1)
        v[ni][nj] = False
    result = max(cnt+1, result)
    return

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

v = [[False for _ in range(M)] for _ in range(N)]
dp = [[-1 for _ in range(M)] for _ in range(N)]
dp[0][0] = 0
# print(arr)
result = 0
dfs(0, 0, 0)

print(result)