"""
구슬게임
dp[k1][k2]: 구슬의 수가 k1, k2일 때 이기는 사람
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

def check_dp(i, j):
    """
    b1, b2, b3 를 뺐을때 세개 다 A가 이기는거면 B
    아니면 A
    """
    for d in b1, b2, b3:
        ni = i - d
        if not (0<=ni<MAX_RANGE):
            continue
        if dp[ni][j] != 'A':
            return False
    for d in b1, b2, b3:
        nj = j - d
        if not (0<=nj<MAX_RANGE):
            continue
        if dp[i][nj] != 'A':
            return False
    return True
    

b1, b2, b3 = map(int, input().split())

MAX_RANGE = 501

dp = [[False for _ in range(MAX_RANGE)] for _ in range(MAX_RANGE)]

dp[b1][0] = 'A'
dp[b2][0] = 'A'
dp[b3][0] = 'A'

dp[0][b1] = 'A'
dp[0][b2] = 'A'
dp[0][b3] = 'A'

for i in range(MAX_RANGE):
    for j in range(MAX_RANGE):
        if dp[i][j]:
            continue
        if check_dp(i, j):
            dp[i][j] = 'B'
        else:
            dp[i][j] = 'A'


for _ in range(5):
    k1, k2 = map(int, input().split())
    print(dp[k1][k2])