def dfs(node, cnt):
    v[node] = True

    if node == b:
        print(cnt)
        exit()

    for nxt in graph[node]:
        if v[nxt]:
            continue
        dfs(nxt, cnt+1)
    v[node] = False

n = int(input())

a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

v = [False for _ in range(n+1)]

dfs(a, 0)
print(-1)