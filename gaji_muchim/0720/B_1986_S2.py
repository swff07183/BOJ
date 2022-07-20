"""
체스
"""
import sys
sys.stdin = open('input.txt')
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int, input().split())

board = [[0 for _ in range(m+1)] for _ in range(n+1)]

# arr = [[] for _ in range(3)]
di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [-1, 0, 1, -1, 1, -1, 0, 1]

ki = [-2, -1, -2, -1, 2, 1, 2, 1]
kj = [-1, -2, 1, 2, -1, -2, 1, 2]

queen = list(map(int, input().split()))
knight = list(map(int, input().split()))
pawn = list(map(int, input().split()))
for x in range(pawn[0]):
    i, j = pawn[x*2+1], pawn[x*2+2]
    board[i][j] = 1

for x in range(knight[0]):
    i, j = knight[x*2+1], knight[x*2+2]
    board[i][j] = 2
    for d in range(8):
        ni = i + ki[d]
        nj = j + kj[d]
        if not (1<=ni<=n and 1<=nj<=m):
            continue
        if board[ni][nj] == 0:
            board[ni][nj] = -1

for x in range(queen[0]):
    i, j = queen[x*2+1], queen[x*2+2]
    board[i][j] = 3
for x in range(queen[0]):
    i, j = queen[x*2+1], queen[x*2+2]
    for d in range(8):
        for k in range(1, n*m):
            ni = i + (di[d]*k)
            nj = j + (dj[d]*k)
            if not (1<=ni<=n and 1<=nj<=m) or board[ni][nj]>0:
                break
            if board[ni][nj] == 0:
                board[ni][nj] = -1

ans = 0
for i in range(1, n+1):
    for j in range(1, m+1):
        if board[i][j]==0:
            ans += 1
print(ans)