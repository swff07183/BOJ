import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start, distance, graph):
    """
    다익스트라 알고리즘
    - 최단 거리 리스트 중 가장 작은 값을 선택한다.
    - 해당 노드 기준으로 거리 체크하고, distance 업데이트
    - 위의 과정을 반복한다.
    """
    queue = []
    distance[start] = 0
    heapq.heappush(queue, (distance[start], start))
    while queue:
        d, node = heapq.heappop(queue)
        if distance[node] < d:
            continue
        for nxt, t in graph[node]:
            # node를 거쳐서 가는 거리 계산
            new_d = distance[node] + t
            # 만약 현재까지 최단 경로보다 새로 구한 거리가 더 짧다면 갱신
            if new_d < distance[nxt]:
                distance[nxt] = new_d
                heapq.heappush(queue, (new_d, nxt))

N, M, X = map(int, input().split())

distance_n = [INF for _ in range(N+1)]
distance_r = [INF for _ in range(N+1)]
graph_n = [[] for _ in range(N+1)]
graph_r = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graph_n[s].append((e, t))
    graph_r[e].append((s, t))

dijkstra(X, distance_n, graph_n)
dijkstra(X, distance_r, graph_r)

result = 0
for i in range(1, N+1):
    result = max(result, distance_n[i] + distance_r[i])
print(result)
