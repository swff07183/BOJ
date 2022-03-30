import sys
sys.stdin = open('input.txt')

N = int(input())

dp = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, N):
    dp[i][0] += dp[i-1][0]
    for j in range(1, i):
        dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
    dp[i][i] += dp[i-1][i-1]

result = max(dp[N-1])
print(result)
