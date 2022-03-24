import sys

sys.stdin = open('input.txt')
# input = sys.stdin.readline

def z_arr(n, si, sj):
    global result
    
    if si == r and sj == c:
        print(result)
        exit(0)

    if n == 1:
        result += 1
        return
    
    if not(si <= r < si+n and sj <= c < sj+n):
        result += n*n
        return

    l = n//2
    z_arr(l, si, sj)
    z_arr(l, si, sj + l)
    z_arr(l, si + l, sj)
    z_arr(l, si + l, sj + l)

N, r, c = map(int, input().split())
width = 2**(N)
# arr = [[0 for _ in range(width)] for _ in range(width)]
result = 0
z_arr(width, 0, 0)
# for row in arr:
#     print(row)