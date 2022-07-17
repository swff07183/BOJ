"""
미로만들기
최대 범위가 50이길래
그냥 101*101 만들어놓고
50, 50 에서 시작함
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]

arr = [['#' for _ in range(101)] for _ in range(101)]

i, j = 50, 50
arr[i][j]='.'
x = [50, 50]
y = [50, 50]
N = int(input())
data = input()
d = 0
for op in data:
    if op=='R':
        d = (d+1) % 4
    if op=='L':
        d = (d-1) % 4
    if op=='F':
        i += di[d]
        j += dj[d]
        arr[i][j] = '.'
        x[0] = min(x[0], i)
        x[1] = max(x[1], i)
        y[0] = min(y[0], j)
        y[1] = max(y[1], j)

for k in range(x[0], x[1]+1):
    print(*arr[k][y[0]:y[1]+1], sep='')


