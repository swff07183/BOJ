import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

INF = int(1e9)

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dijkstra():
    queue = []
    distance[0][0] = arr[0][0]
    heapq.heappush(queue, [distance[0][0], 0, 0])
    while queue:
        d, i, j = heapq.heappop(queue)
        if d > distance[i][j]:
            continue
        for idx_d in range(4):
            ni = i + di[idx_d]
            nj = j + dj[idx_d]
            if not (0<=ni<N and 0<=nj<N):
                continue

            new_d = distance[i][j] + arr[ni][nj]
            if new_d < distance[ni][nj]:
                distance[ni][nj] = new_d
                heapq.heappush(queue, [new_d, ni, nj])

tc = 1
while True:
    N = int(input())    # 동굴의 크기
    if N == 0:  # 종료 조건
        break
    
    arr = [list(map(int, input().split())) for _ in range(N)]
    distance = [[INF for _ in range(N)] for _ in range(N)]

    dijkstra()
    print(f'Problem {tc}: {distance[N-1][N-1]}')
    tc += 1