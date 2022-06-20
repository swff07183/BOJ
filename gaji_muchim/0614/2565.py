# 2565 전깃줄
"""
A 기준으로 오름차순 정렬하고
B 기준으로 가장 긴 증가하는 부분수열
"""
import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = []
for _ in range(N):
    a, b = map(int, input().split())
    arr.append([a, b])
arr.sort()  # A 기준으로 정렬

dp = [0 for _ in range(N)]
dp[0] = 1
for i in range(1, N):
    max_dp = 0
    for j in range(i):
        # 나보다 앞에있는거 중에서
        # 나보다 작은것 중 dp값 제일 큰거 가져와서 저장
        if arr[i][1] > arr[j][1]:
            max_dp = max(max_dp, dp[j])
    dp[i] = max_dp + 1
    
print(N-max(dp))