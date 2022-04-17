import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(N+1)]
seq = [[x] for x in range(N+1)]
dp[1] = 0
for i in range(2, N+1):
    tmp = dp[i-1]
    seq[i] = [i] + seq[i-1]
    if i%3 == 0:
        if dp[i//3] < tmp:
            tmp = dp[i//3]
            seq[i] = [i] + seq[i//3]
    if i%2 == 0:
        if dp[i//2] < tmp:
            tmp = dp[i//2]
            seq[i] = [i] + seq[i//2]

    dp[i] = tmp + 1

print(dp[N])
print(*seq[N])