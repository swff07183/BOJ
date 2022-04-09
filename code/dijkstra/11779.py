import sys,heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    # 경로도 같이 넣어주자..!
    queue = []
    distance[start] = [0, [start]]
    heapq.heappush(queue, [0, [start]])

    while queue:
        d, node_li = heapq.heappop(queue)
        node = node_li[-1]
        if d > distance[node][0]:
            continue
        for nxt, cost in arr[node]:
            new_d = d + cost
            if new_d < distance[nxt][0]:
                distance[nxt] = [new_d, distance[node][1] + [nxt]]
                heapq.heappush(queue, [new_d, distance[node][1] + [nxt]])




n = int(input())
m = int(input())
distance = [[INF, []] for _ in range(n+1)]
arr = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])
s, e = map(int, input().split())
dijkstra(s)
result, nodes = distance[e]
print(result)
print(len(nodes))
print(*nodes)