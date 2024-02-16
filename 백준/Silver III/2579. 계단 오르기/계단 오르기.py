N = int(input())

arr = [0] + [int(input()) for _ in range(N)] + [0, 0, 0]
dp = [0 for _ in range(N+10)]
dp[1] = arr[1]
dp[2] = arr[1] + arr[2]

for n in range(3, N+1):
    """
    n-3, n-1, n
    n-2, n
    """
    dp[n] = max(arr[n] + arr[n-1] + dp[n-3], dp[n-2] + arr[n])

print(dp[N])