import sys
input = lambda : sys.stdin.readline().rstrip()

N, K = map(int, input().split())
arr = [(0, 0)]
for _ in range(N):
    w, v = map(int, input().split())
    arr.append([w, v])

dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    w, v = arr[i]
    for j in range(K+1):
        if j-w >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])