import sys
input = lambda : sys.stdin.readline().rstrip()

def get_cnt(x1, y1, x2, y2):
    ret = 0
    for i in range(1, 11):
        tmp = cnt[x2][y2][i] - cnt[x1-1][y2][i] - cnt[x2][y1-1][i] + cnt[x1-1][y1-1][i]
        if tmp:
            ret += 1
    return ret

N = int(input())
arr = [[0 for _ in range(N+1)]] + [[0] + list(map(int, input().split())) for _ in range(N)]
cnt = [[[0 for _ in range(11)] for _ in range(N+1)] for _ in range(N+1)]


for i in range(N+1):
    cnt[i][0] = [0 for _ in range(11)]
    cnt[0][i] = [0 for _ in range(11)]

for i in range(1, N+1):
    for j in range(1, N+1):
        for k in range(1, 11):
            cnt[i][j][k] = cnt[i][j-1][k] + cnt[i-1][j][k] - cnt[i-1][j-1][k]
        cnt[i][j][arr[i][j]] += 1


Q = int(input())
for _ in range(Q):
    x1, y1, x2, y2 = map(int, input().split())
    result = get_cnt(x1, y1, x2, y2)
    print(result)