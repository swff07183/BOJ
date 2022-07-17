import sys
input = lambda: sys.stdin.readline().rstrip()

N = 100

"""
끝자리가 0인거, 1인거 다르게 카운트
dp[i][j][0]: i자리 수 중 인접한 비트의 개수가 j이고 끝이 0인거
dp[i][j][1]: ~~ 끝이 1인거
"""
dp = [[[0, 0] for _ in range(N+1)] for _ in range(N+1)]

dp[1][0][0] = 1
dp[1][0][1] = 1

for i in range(2, N+1):
    # 일단 100까지 인접한 비트의 개수가 0인거 다 세주기
    dp[i][0][0] = dp[i-1][0][0] + dp[i-1][0][1]
    dp[i][0][1] = dp[i-1][0][0]

for i in range(2, N+1):
    for j in range(1, N+1):
        """
        dp[i][j][0]: i-1자리이고 인.비.개 j인 숫자 뒤에 0 다 붙이면
        dp[i][j][1]: i-1자리이고 j-1이고 1로 끝나는 숫자 뒤에 1 붙인거
                        + i-1자리 j이고 0으로 끝나는 숫자 뒤에 1 붙인거
        """
        dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1]
        dp[i][j][1] = dp[i-1][j-1][1] + dp[i-1][j][0]

for i in range(1, 10):
    print(f'{i}: ', end=' ')
    for j in range(0, 10):
        print(f'{sum(dp[i][j]):3}', end=' ')
    print()