import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    """
    다익스트라 알고리즘
    - 최단 거리 리스트 중 가장 작은 값을 선택한다.
    - 해당 노드 기준으로 거리 체크하고, distance 업데이트
    - 위의 과정을 반복한다.
    """
    queue = []
    distance[start][start] = 0
    heapq.heappush(queue, (distance[start][start], start))
    while queue:
        d, node = heapq.heappop(queue)
        if distance[start][node] < d:
            continue
        for nxt, w in graph[node]:
            # node를 거쳐서 가는 거리 계산
            new_d = distance[start][node] + w
            # 만약 현재까지 최단 경로보다 새로 구한 거리가 더 짧다면 갱신
            if new_d < distance[start][nxt]:
                distance[start][nxt] = new_d
                heapq.heappush(queue, (distance[start][nxt], nxt))

N, M, X = map(int, input().split())
# v = [False for _ in range(N+1)]
distance = [[INF for _ in range(N+1)] for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    graph[s].append((e, t))

for i in range(1, N+1):
    dijkstra(i)

result = 0  # 왕복 거리 최대값 저장할 변수
for i in range(1, N+1):
    d = distance[i][X] + distance[X][i]
    if d > result:
        result = d

print(d)