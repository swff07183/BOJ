"""
함께 블록 쌓기
N : 1000, M: 10
완탐해버리면 10^1000. 절대 안된다.
백트래킹 가능? 일단 해봄 -> 바로 시간초과
DP 고
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, H = map(int, input().split())
arr = [[0] + list(map(int, input().split())) for _ in range(N)]

dp = [[0 for _ in range(N)] for _ in range(H+1)]

for i in arr[0]:
    dp[i][0] = 1

    
for i in range(1, N):
    for j in range(H+1):
        for k in arr[i]:
            if j-k < 0:
                continue
            dp[j][i] += dp[j-k][i-1]

ans = dp[H][N-1] % 10007
print(ans)



# def block(cnt, total, tmp=[]):
#     global ans
#     if cnt == N and total == H:
#         ans += 1
#         return
#     if cnt >= N:
#         return

#     for i in range(len(arr[cnt])):
#         block(cnt+1, total + arr[cnt][i], tmp + [arr[cnt][i]])

# N, M, H = map(int, input().split())
# arr = [[0] + list(map(int, input().split())) for _ in range(N)]

# ans = 0
# block(0, 0)
# print(ans)