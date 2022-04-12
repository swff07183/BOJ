import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    queue = []
    distance = [INF for _ in range(N+1)]
    distance[start] = 0
    heapq.heappush(queue, (0, start))
    
    while queue:
        d, node = heapq.heappop(queue)
        if d > distance[node]:
            continue
        for nxt, c in graph[node]:
            new_d = d + c
            if new_d < distance[nxt]:
                distance[nxt] = new_d
                heapq.heappush(queue, (new_d, nxt))
    
    return distance


N, E = map(int, input().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())
result = 0
d0 = dijkstra(1)                # d0 : 1번 노드에서 다른 노드간의 최단 경로
d1 = dijkstra(v1)               # d1 : v1 노드에서 다른 노드간의 최단 경로
d2 = dijkstra(v2)               # d2 : v2 노드에서 다른 노드간의 최단 경로
result = min(               
    d0[v1]+d1[v2]+d2[N],        # 1 -> v1 -> v2 -> N
    d0[v2]+d2[v1]+d1[N]         # 1 -> v2 -> v1 -> N
    )                           # 두개 중에 작은 값 결과로 저장하기

if result >= INF:               # 갈 수 없는 경우라면, -1
    result = -1
print(result)