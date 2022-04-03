import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, prv):
    size[node] = 1
    for nxt in tree[node]:
        if nxt != prv:
            size[node] += dfs(nxt, node)
    
    return size[node]

N, R, Q = map(int, input().split())
tree = [[] for _ in range(N+1)]
size = [0 for _ in range(N+1)]

for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dfs(R, -1)

for _ in range(Q):
    print(size[int(input())])
