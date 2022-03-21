import sys
sys.setrecursionlimit(10**5)

def dfs(start, total):
    global max_length, max_node
    if max_length < total:
        max_length = total
        max_node = start
    for node, w in arr[start]:
        if v[node]==0:
            v[node] = 1
            dfs(node, total + w)
            v[node] = 0
    return

n = int(input())
arr = [[] for _ in range(n+1)]
v = [0 for _ in range(n+1)]
for _ in range(n-1):
    p, c, w = map(int, input().split())
    arr[p].append((c, w))
    arr[c].append((p, w))

max_length = 0
max_node = -1

v[1] = 1
dfs(1, 0)
v = [0 for _ in range(n+1)]
v[max_node] = 1
dfs(max_node, 0)
print(max_length)