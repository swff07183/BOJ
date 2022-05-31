from collections import deque

def topology():
    queue = deque()
    result = []

    for i in range(1, N+1):
        if indegree[i] == 0:
            queue.append(i)
    while queue:
        node = queue.popleft()
        result.append(node)
        for nxt in arr[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    
    return result

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
result = []

for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    indegree[b] += 1

result = topology()
print(*result)