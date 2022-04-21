import sys
input = sys.stdin.readline

INF = 1000000

N, M = map(int, input().split())
arr = [0] + list(map(int, input().split()))
v = []
for i in range(M):
    for j in range(i + 1, M + 1):
        v.append(arr[i] + arr[j])
dp = [INF for _ in range(20001)]
for w in v:
    dp[w] = 1


for i in range(1, N+1):
    for w in v:
        if i-w < 0:
            continue
        dp[i] = min(dp[i], dp[i-w] + 1)
if dp[N] == INF:
    print(-1)
else:
    print(dp[N])