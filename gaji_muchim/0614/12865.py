# 12865 평범한 배낭
"""
knapsack
"""
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
        # 넣을수있으면
        # 넣는거랑 안넣는거랑 뭐가 더 큰지 비교해서 저장
        if j-w >= 0:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)
        # 가방무게보다 물건 무게가 더 크면 무게 그대로
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])