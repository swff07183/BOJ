from collections import deque

def topology():
    queue = deque()
    result = []
    for i in range(1, N+1):
        if indegree[i] == 0:
            result.append(i)
            queue.append(i)
    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                result.append(nxt)
                queue.append(nxt)
            dp[nxt] = max(arr[nxt] + dp[node], dp[nxt])
    
    return result

N = int(input())
graph = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]
dp = [0 for _ in range(N+1)]
arr = [0 for _ in range(N+1)]
for i in range(1, N+1):
    data = list(map(int, input().split()))
    dp[i] = data[0]
    arr[i] = data[0]
    for node in data[1:]:
        if node == -1:
            break
        graph[node].append(i)
        indegree[i] += 1


result = topology()
for t in dp[1:]:
    print(t)