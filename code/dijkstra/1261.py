import heapq, sys
input = sys.stdin.readline

INF = int(1e9)
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dijkstra():
    queue = []
    distance = [[INF for _ in range(M)] for _ in range(N)]
    heapq.heappush(queue, [0, 0, 0])
    distance[0][0] = 0

    while queue:
        d, i, j = heapq.heappop(queue)
        if distance[i][j] < d:
            continue
        for idx_d in range(4):
            ni = i + di[idx_d]
            nj = j + dj[idx_d]
            if not (0<=ni<N and 0<=nj<M):
                continue
            new_d = d + arr[ni][nj]
            if distance[ni][nj] > new_d:
                distance[ni][nj] = new_d
                heapq.heappush(queue, [new_d, ni, nj])
    

    return distance[N-1][M-1]


M, N = map(int, input().split())


arr = [list(map(int, list(input().rstrip()))) for _ in range(N)]

result = dijkstra()
print(result)