import sys, heapq
input = sys.stdin.readline

INF = int(1e9)

def dijkstra():
    distance = [INF for _ in range(N+1)]
    distance[s] = 0
    queue = []
    heapq.heappush(queue, [s, 0])

    while queue:
        node, d = heapq.heappop(queue)
        if d > distance[node]:
            continue
        for nxt, nxt_d in graph[node]:
            new_d = d + nxt_d
            if distance[nxt] > new_d:
                distance[nxt] = new_d
                heapq.heappush(queue, [nxt, new_d])
    
    return distance[e]


N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, d = map(int, input().split())
    graph[a].append([b, d])

s, e = map(int, input().split())
result = dijkstra()
print(result)