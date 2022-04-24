import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline
INF = int(1e9)

di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]

def dijkstra(si, sj):
    queue = []
    distance = [[[INF for _ in range(N)] for _ in range(N)] for _ in range(4)]
    for d in range(4):
        distance[d][si][sj] = 0
        heapq.heappush(queue, [0, si, sj, d])

    while queue:
        cnt, i, j, d = heapq.heappop(queue)
        ni = i + di[d]
        nj = j + dj[d]
        if not (0<=ni<N and 0<=nj<N) or arr[ni][nj] == '*' or cnt >= distance[d][ni][nj]:
            continue
        
        distance[d][ni][nj] = cnt
        # "!" 인 경우
        if arr[ni][nj] == '!':
            d1 = (d+1) % 4
            d2 = (d+3) % 4
            heapq.heappush(queue, [cnt+1, ni, nj, d1])
            heapq.heappush(queue, [cnt+1, ni, nj, d2])

        # "." 인 경우
        heapq.heappush(queue, [cnt, ni, nj, d])
    
    
    return min(distance[i][ei][ej] for i in range(4))


N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]
v = [[False for _ in range(N)] for _ in range(N)]

p = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '#':
            p.append((i, j))
si, sj = p[0]
ei, ej = p[1]

print(dijkstra(si, sj))