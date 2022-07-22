"""
공룡게임
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

if N==1:
    print(0)
    exit()
if N==2:
    print(1)
    exit()

dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(N+1)]

for i in range(3):
    for j in range(3):
        dp[2][i][j] = 1

dp[2][2][2] = 0

for c in range(3, N+1):
    dp[c][0][0] = dp[c-1][0][0] + dp[c-1][1][0] + dp[c-1][2][0]
    dp[c][0][1] = dp[c-1][0][0] + dp[c-1][1][0] + dp[c-1][2][0]
    dp[c][0][2] = dp[c-1][0][0] + dp[c-1][1][0] + dp[c-1][2][0]

    dp[c][1][0] = dp[c-1][0][1] + dp[c-1][1][1] + dp[c-1][2][1]
    dp[c][1][1] = dp[c-1][0][1]
    dp[c][1][2] = dp[c-1][0][1]

    dp[c][2][0] = dp[c-1][0][2] + dp[c-1][1][2]
    dp[c][2][1] = dp[c-1][0][2]


dp2 = [[[0 for _ in range(2)] for _ in range(2)] for _ in range(N+1)]

for i in range(2):
    for j in range(2):
        dp2[2][i][j] = 1

for c in range(3, N+1):
    dp2[c][0][0] = dp2[c-1][0][0] + dp2[c-1][1][0]
    dp2[c][0][1] = dp2[c-1][0][0] + dp2[c-1][1][0]
    dp2[c][1][0] = dp2[c-1][0][1] + dp2[c-1][1][1]
    dp2[c][1][1] = dp2[c-1][0][1]

ans = (sum(sum(dp[N-1], [])) - sum(sum(dp2[N-1], []))) % 1_000_000_007

print(ans)