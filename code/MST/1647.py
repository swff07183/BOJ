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
    if x == y:
        return
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1


N, M = map(int, input().split())

p = [x for x in range(N+1)]
rank = [0 for _ in range(N+1)]

arr = [tuple(map(int, input().split())) for _ in range(M)]

arr.sort(key=lambda x:x[2])

cnt = 0
total = 0
i = 0
while cnt < N-2:
    a, b, c = arr[i]
    if find_(a) != find_(b):
        union_(a, b)
        cnt += 1
        total += c
    i += 1
print(total)