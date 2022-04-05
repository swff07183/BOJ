input = sys.stdin.readline

def find_set(x):
    if p[x] == x:
        return x
    else:
        p[x] = find_set(p[x])
        return p[x]

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x < y:
        p[y] = x
    elif x > y:
        p[x] = y


V, E = map(int, input().split())
data = [tuple(map(int, input().split())) for _ in range(E)]
p = [x for x in range(V+1)]
data.sort(key=lambda x: x[2])

cnt = 0
result = 0
i = 0
while cnt < V-1:
    s, e, w = data[i]
    i += 1
    if find_set(s) == find_set(e):
        continue
    union(s, e)
    cnt += 1
    result += w
print(result)