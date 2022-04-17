import sys
input = sys.stdin.readline
from collections import deque

def bfs(a, b, c):
    queue = deque()
    queue.append([a, b, c])
    while queue:
        a, b, c = queue.popleft()
        if a==b and b==c:
            return 1
        if a > b:
            na, nb, nc = a-b, b+b, c
            if not v[na][nb]:
                v[na][nb] = True
                queue.append([na, nb, nc])
        elif a < b:
            na, nb, nc = a+a, b-a, c
            if not v[na][nb]:
                v[na][nb] = True
                queue.append([na, nb, nc])
        if b > c:
            na, nb, nc = a, b-c, c + c
            if not v[na][nb]:
                v[na][nb] = True
                queue.append([na, nb, nc])
        elif b < c:
            na, nb, nc = a, b+b, c-b
            if not v[na][nb]:
                v[na][nb] = True
                queue.append([na, nb, nc])
        if a > c:
            na, nb, nc = a-c, b, c + c
            if not v[na][nb]:
                v[na][nb] = True
                queue.append([na, nb, nc])
        elif a < c:
            na, nb, nc = a+a, b, c-a
            if not v[na][nb]:
                v[na][nb] = True
                queue.append([na, nb, nc])
    
    return 0

a, b, c = map(int, input().split())
v = [[False for _ in range(1001)] for _ in range(1001)]

print(bfs(a, b, c))