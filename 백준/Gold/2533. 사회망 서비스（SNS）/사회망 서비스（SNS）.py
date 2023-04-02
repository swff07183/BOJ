import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

def dfs(node):
    for nxt in tree[node]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        dfs(nxt)
        dp[node][0] += dp[nxt][1]
        dp[node][1] += min(dp[nxt][0], dp[nxt][1])
    

N = int(input())
tree = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
# dp[x][0] : x번 노드 선택 X, dp[x][1] : x번 노드 선택
dp = [[0, 1] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

visited[1] = True
dfs(1)
print(min(dp[1]))