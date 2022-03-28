import sys
input = sys.stdin.readline

def dfs(node, total):
    global result, end
    if result != -1:
        return
    if end == node:
        result = total
        return
    for n, d in arr[node]:
        if not v[n]:
            v[n] = 1
            dfs(n, total + d)
            v[n] = 0
    return
    


N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for i in range(N-1):
    s, e, d = map(int, input().split())
    arr[s].append((e, d))
    arr[e].append((s, d))

for _ in range(M):
    start, end = map(int, input().split())
    v = [0 for _ in range(N+1)]
    result = -1
    v[start] = 1
    dfs(start, 0)
    print(result)
