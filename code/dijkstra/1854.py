import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    queue = []
    distance[start][0] = 0
    heapq.heappush(queue, [0, start])

    while queue:
        d, node = heapq.heappop(queue)
        for nxt, w in arr[node]:
            new_d = d + w
            if distance[nxt][k-1] > new_d:
                distance[nxt][k-1] = new_d
                distance[nxt].sort()
                heapq.heappush(queue, [new_d, nxt])
    
    return


n, m, k = map(int, input().split())
arr = [[] for _ in range(n+1)]
distance = [[INF for _ in range(k+1)] for _ in range(n+1)]
dk = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a].append([b, c])

dijkstra(1)
# for row in distance:
#     print(row)
for i in range(1, n+1):
    if distance[i][k-1] == INF:
        print(-1)
    else:
        print(distance[i][k-1])