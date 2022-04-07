import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def get_depth(node):
    if depth[node] != -1:
        return depth[node]
    if p[node] == node:
        depth[node] = 0
        return 0
    else:
        depth[node] = get_depth(p[node]) + 1
        return depth[node]

def lca(a, b):
    # 깊이 맞추기
    while depth[a] > depth[b]:
        a = p[a]
    while depth[a] < depth[b]:
        b = p[b]
    while a != b:
        a = p[a]
        b = p[b]
    return a

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    p = [x for x in range(N+1)]
    depth = [-1 for x in range(N+1)]
    for _ in range(N-1):
        a, b = map(int, input().split())
        p[b] = a

    for i in range(1, N+1):
        get_depth(i)
    
    n1, n2 = map(int, input().split())
    print(lca(n1, n2))