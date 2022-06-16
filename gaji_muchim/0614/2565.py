import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])
arr.sort()

dp = [0 for _ in range(N)]
dp[0] = 1
for i in range(1, N):
    max_dp = 0
    for j in range(i):
        if arr[i][1] > arr[j][1]:
            max_dp = max(max_dp, dp[j])
    dp[i] = max_dp + 1
print(N-max(dp))