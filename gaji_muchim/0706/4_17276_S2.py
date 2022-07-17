"""
이거 뭐 그냥 구현했음
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

def rot_45(arr):
    tmp = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        tmp[i][mid] = arr[i][i]
        tmp[i][n-i-1] = arr[i][mid]
        tmp[mid][n-i-1] = arr[i][n-i-1]
        arr[i][i] = arr[mid][i]
    
    for i in range(n):
        for j in range(n):
            if not tmp[i][j]:
                tmp[i][j] = arr[i][j]
    
    return tmp

T = int(input())

for _ in range(T):
    n, d = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    mid = n//2
    
    if d < 0:
        d += 360
    ans = arr
    for i in range(d//45):
        ans = rot_45(ans)
    

    for row in ans:
        print(*row)