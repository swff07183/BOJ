N = int(input())

dp = [[0 for _ in range(2)] for _ in range(91)]

dp[1][1] = 1
dp[1][0] = 0
dp[2][1] = 0
dp[2][0] = 1
for i in range(3, N+1):
    dp[i][0] = dp[i-1][1] + dp[i-1][0]
    dp[i][1] = dp[i-1][0]*1

print(dp[N][0] + dp[N][1])