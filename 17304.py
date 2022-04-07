import sys
sys.stdin = open('input.txt')

def dfs(node, prv):
    global cnt
    for nxt in arr[node]:
        #if arr[node][nxt] == 1 and arr[nxt][node] == 0:
        if node not in arr[nxt]:
            if not v[nxt]:
                cnt += 1
            v[nxt] = 1
            arr[node][nxt] = 0
            dfs(nxt)
            

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
v = [0 for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)

cnt = 0