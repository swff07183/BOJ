import sys, heapq
sys.stdin = open('input.txt')

INF = int(1e9)

def dijkstra(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, [0, start])
    while queue:
        d, node = heapq.heappop(queue)
        for nxt, s in graph[node]:
            new_d = d + s
            if distance[nxt] > new_d:
                distance[nxt] = new_d
                heapq.heappush(queue, [new_d, nxt])

T = int(input())
for tc in range(1, T+1):
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    distance = [INF for _ in range(n+1)]
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append([a, s])
    
    dijkstra(c)
    cnt = 0
    result = 0
    for c in distance[1:]:
        if c == INF:
            continue
        cnt += 1
        result = max(result, c)
    
    print(cnt, result)
