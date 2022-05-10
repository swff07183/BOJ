import sys
input = sys.stdin.readline

INF = int(1e9)

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[INF, INF, INF] for _ in range(N)] for _ in range(3)]
dp[0][0] = [arr[0][0], INF, INF]
dp[1][0] = [INF, arr[0][1], INF]
dp[2][0] = [INF, INF, arr[0][2]]

for k in range(3):
    for i in range(1, N):
        for j, a, b in [(0, 1, 2), (1, 2, 0), (2, 0, 1)]:
            tmp = min(dp[k][i-1][a], dp[k][i-1][b])
            dp[k][i][j] = arr[i][j] + tmp

result = INF

for k in range(3):
    a = (k+1) % 3
    b = (k+2) % 3
    result = min(result, dp[k][N-1][a], dp[k][N-1][b])
print(result)
for k in range(3):
    for row in dp[k]:
        print(*row)
    print("="*70)
