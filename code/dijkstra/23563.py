import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

INF = int(1e9)

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dijkstra(si, sj):
    queue = []
    distance[si][sj] = 0
    heapq.heappush(queue, [0, si, sj])

    while queue:
        d, i, j = heapq.heappop(queue)
        if d > distance[i][j]:
            continue
        for idx_d in range(4):
            ni = i + di[idx_d]
            nj = j + dj[idx_d]
            if arr[ni][nj] == '#':
                continue
            new_d = d if check_wall(i, j) and check_wall(ni, nj) else d + 1
            if new_d < distance[ni][nj]:
                distance[ni][nj] = new_d
                heapq.heappush(queue, [new_d, ni, nj])
    return


def check_wall(i, j):
    return arr[i+1][j] == '#' or arr[i-1][j] == '#' or arr[i][j+1] == '#' or arr[i][j-1] == '#'


H, W = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(H)]
distance = [[INF for _ in range(W)] for _ in range(H)]
for i in range(H):
    for j in range(W):
        if arr[i][j] == 'S':
            start = (i, j)
        if arr[i][j] == 'E':
            end = (i, j)

dijkstra(*start)
print(distance[end[0]][end[1]])


# for row in arr:
#     print(*row)
# print("=" * 50)

# for row in distance:
#     for d in row:
#         if d==INF:
#             print("#", end=' ')
#         else:
#             print(d, end=' ')
#     print()