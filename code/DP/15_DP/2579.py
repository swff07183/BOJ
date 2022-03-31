N = int(input())
arr = [0]+[int(input()) for _ in range(N)]
dp = [0 for _ in range(N+1)]

try:
    dp[0] = 0
    dp[1] = arr[1]
    dp[2] = arr[1] + arr[2]
except IndexError:
    pass

for i in range(3, N+1):
    dp[i] = max(dp[i-2]+arr[i], dp[i-3] + arr[i]+arr[i-1])

print(dp[N])