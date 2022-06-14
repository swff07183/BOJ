import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(50010)

def lca(a, b):
    while depth[a] > depth[b]:
        a = p[a]
    while depth[b] > depth[a]:
        b = p[b]
    while a != b:
        a = p[a]
        b = p[b]
    return a

def dfs(node, cnt):
    v[node] = True
    depth[node] = cnt
    for nxt in graph[node]:
        if v[nxt]:
            continue
        p[nxt] = node
        dfs(nxt, cnt+1)

N = int(input())

graph = [[] for _ in range(N+1)]
p = [-1 for _ in range(N+1)]
v = [False for _ in range(N+1)]
depth = [0 for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(1, 0)
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))