import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def find_set(x):
    if x == p[x]:
        return x
    else:
        parent = find_set(p[x])
        p[x] = parent
        return p[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x > y:
        p[x] = y
    else:
        p[y] = x

n, m = map(int, input().split())

p = [x for x in range(n+1)]
# print(p)
for _ in range(m):
    oper, a, b = map(int, input().split())
    if oper == 0:
        union(a, b)
    else:
        if find_set(a) == find_set(b):
            print("YES")
        else:
            print("NO")