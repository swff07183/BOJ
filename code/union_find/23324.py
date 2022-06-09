import sys
input = lambda: sys.stdin.readline().rstrip()

def find_(x):
    if x != p[x]:
        p[x] = find_(p[x])
    return p[x]

def union_(x, y):
    x = find_(x)
    y = find_(y)
    if x > y:
        p[x] = y
        size[y] += size[x]
    elif x < y:
        p[y] = x
        size[x] += size[y]

N, M, K = map(int, input().split())
p = [x for x in range(N+1)]
size = [1 for _ in range(N+1)]

for i in range(1, M+1):
    u, v = map(int, input().split())
    if i==K:
        node1, node2 = u, v
        continue
    union_(u, v)
node1 = find_(node1)
node2 = find_(node2)
if node1 == node2:
    result = 0
else:
    result = size[node1] * size[node2]
print(result)
