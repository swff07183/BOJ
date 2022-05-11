import sys
input = sys.stdin.readline

def find_(x):
    if p[x] == x:
        return x
    else:
        p[x] = find_(p[x])
        return p[x]

def union_(x, y):
    x = find_(x)
    y = find_(y)

    if x==y:
        return
    elif x > y:
        p[x] = y
    else:
        p[y] = x


N, M = map(int, input().split())
arr = ['#'] + input().split()

data = [tuple(map(int, input().split())) for _ in range(M)]
data.sort(key=lambda x:x[2])
p = [i for i in range(N+1)]

cnt = 0
total = 0

for u, v, d in data:
    if arr[u] == arr[v]:
        continue
    u = find_(u)
    v = find_(v)
    if u==v:
        continue
    union_(u, v)
    cnt += 1
    total += d

    if cnt == N-1:
        print(total)
        exit(0)

print(-1)
