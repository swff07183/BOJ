"""
3 5
damir
marko
darko

  d    (0,0)
 m a   (1,0), (0,1)
d a m  (2,0), (1,1), (0, 2)
 a r i
  r k r
   k o
    o


    r
   i o
  m k o
 a r k
d a r
 m a
  d
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

def rot_90(arr):
    """
    90도 돌리면 열과 행 개수가 바뀐다
    """
    r = len(arr)
    c = len(arr[0])
    tmp = [['' for _ in range(r)] for _ in range(c)]
    for i in range(r):
        for j in range(c):
            tmp[j][r-i-1] = arr[i][j]
    return tmp

def rot_45(arr):
    tmp = {}
    r = len(arr)
    c = len(arr[0])
    for i in range(r):
        for j in range(c):
            k = i+j-(r-1)
            tmp[k] = [arr[i][j]] + tmp.get(k, [])
    tmp = sorted(tmp.items(), key=lambda x:x[0])

    for blank, chars in tmp:
        print(' ' * abs(blank), end='')
        print(*chars)


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
K = int(input())

ans = arr

for _ in range(K//90):
    ans = rot_90(ans)
K %= 90
if K:
    rot_45(ans)
else:
    for row in ans:
        print(*row, sep='')