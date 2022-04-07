import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    queue = []
    distance[start][start] = 0
    heapq.heappush(queue, (distance[start][start], start))
    while queue:
        d, node = heapq.heappop(queue)
        if distance[start][node] < d:
            continue
        for nxt, t in graph[node]:
            new_d = distance[start][node] + t
            if new_d < distance[start][nxt]:
                distance[start][nxt] = new_d
                heapq.heappush(queue, (new_d, nxt))

N, M, X = map(int, input().split())
distance = [[INF for _ in range(N+1)] for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

for i in range(1, N+1):
    dijkstra(i)

result = 0
for i in range(1, N+1):
    result = max(result, distance[i][X] + distance[X][i])

print(result)