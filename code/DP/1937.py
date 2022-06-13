import sys
input = lambda: sys.stdin.readline().rstrip()

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

data = []

for i in range(N):
    for j in range(N):
        data.append([arr[i][j], i, j])

data.sort(key=lambda x:-x[0])
result = 0
for c, i, j in data:
    max_dp = 0
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if not (0<=ni<N and 0<=nj<N) or arr[ni][nj] <= c:
            continue
        max_dp = max(max_dp, dp[ni][nj])
    dp[i][j] = max_dp + 1
    result = max(result, dp[i][j])

print(result)