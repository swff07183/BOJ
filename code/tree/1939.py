import sys
input = sys.stdin.readline

def find_(x):
    if x == p[x]:
        return x
    else:
        p[x] = find_(p[x])
        return p[x]

def union_(x, y):
    x = find_(x)
    y = find_(y)
    if rank[x] < rank[y]:
        p[x] = y
    else:
        p[y] = x
        if rank[x] == rank[y]:
            rank[x] += 1

N, M = map(int, input().split())
p = [x for x in range(N+1)]
rank = [0 for _ in range(N+1)]
v = [list(map(int, input().split())) for _ in range(M)]
s, e = map(int, input().split())

v.sort(key=lambda x: -x[2])

for i in range(M):
    a, b, c = v[i]
    union_(a, b)
    if find_(s) == find_(e):
        print(c)
        break