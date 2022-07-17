"""
왜 row, col 바뀌어있음? 개화난다
감싸져있는부분 어떻게함? 어렵다
->
그냥 밖에 패딩 하나 줘서 밖에서 탐색하자
"""

import sys
sys.setrecursionlimit(10**5)
input = lambda: sys.stdin.readline().rstrip()

delta = {
    # j 홀수, 짝수에 따라 구분
    0: [[-1, -1], [-1, 0], [0, 1], [1, 0], [1, -1], [0, -1]],
    1: [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [0, -1]],
}

def in_range(i, j):
    return (0<=i<H+2 and 0<=j<W+2)

def check(i, j):
    total = 0
    idx = i%2
    for d in range(6):              # 6방향 탐색
        ni = i + delta[idx][d][0]
        nj = j + delta[idx][d][1]
        if not in_range(ni, nj):
            continue
        if arr[ni][nj]:
            total += 1
    return total

def dfs(i, j):
    global ans
    v[i][j] = True

    idx = i%2
    tmp = check(i, j)
    ans += tmp
    # print(f'({j}, {i}), {arr[i][j]}, {tmp}')
    for d in range(6):
        ni = i + delta[idx][d][0]
        nj = j + delta[idx][d][1]
        if not in_range(ni, nj):
            continue
        elif not v[ni][nj] and arr[ni][nj]==0:
            dfs(ni, nj)


W, H = map(int, input().split())

arr = [[0 for _ in range(W+2)]]\
    + [[0] + list(map(int, input().split())) + [0] for _ in range(H)]\
    + [[0 for _ in range(W+2)]]

v = [[False for _ in range(W+2)] for _ in range(H+2)]

ans = 0

dfs(0, 0)


print(ans)