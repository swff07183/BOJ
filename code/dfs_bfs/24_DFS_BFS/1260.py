def dfs(start):
    if start == V:
        print(start, end=" ")
        visited[V] = True
    for i in range(1, N+1):
        if visited[i] == 0 and arr[start][i]:
            visited[i] = 1
            print(i, end=" ")
            dfs(i)
    return

def bfs(V):
    queue = []
    visited_bfs = [0 for _ in range(N+1)]
    queue.append(V)
    while len(queue) > 0:
        node = queue.pop(0)
        if visited_bfs[node] == 0:
            visited_bfs[node] = 1
            print(node, end=" ")
            for i in range(1, N+1):
                if arr[node][i] and visited_bfs[i] == 0:
                    queue.append(i)


N, M, V = map(int, input().split())

arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    arr[s][e] = 1
    arr[e][s] = 1


dfs(V)
print()
bfs(V)