from collections import deque

def bfs(root):
    queue = deque()
    queue.append(root)
    parent[root] = -1
    while queue:
        node = queue.popleft()
        for i in arr[node]:
            if parent[i] == 0:
                queue.append(i)
                parent[i] = node
                
    return

N = int(input())
arr = [[] for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

for i in range(N-1):
    node1, node2 = map(int, input().split())
    arr[node1].append(node2)
    arr[node2].append(node1)

bfs(1)
for i in range(2, N+1):
    print(parent[i])