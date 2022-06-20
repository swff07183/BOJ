import sys, heapq
input = lambda : sys.stdin.readline().rstrip()

INF = int(1e9)

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def dijkstra():
    distance = [[INF for _ in range(n)] for _ in range(n)]
    queue = []
    distance[s[0]][s[1]] = 0
    heapq.heappush(queue, [0, s[0], s[1]])

    while queue:
        d, i, j = heapq.heappop(queue)
        if distance[i][j] < d:
            continue
        for idx_d in range(4):
            ni = i + di[idx_d]
            nj = j + dj[idx_d]
            if not (0<=ni<n and 0<=nj<n):
                continue
            new_d = d + (not arr[ni][nj])
            if new_d < distance[ni][nj]:
                distance[ni][nj] = new_d
                heapq.heappush(queue, [new_d, ni, nj])
    
    return distance[n-1][n-1]


    

n = int(input())
arr = [list(map(int, input())) for _ in range(n)]
s = [0, 0]
e = [n-1, n-1]

result = dijkstra()
print(result)

"""
dijkstra
ㅁ -> 검은방 : 가중치 0
ㅁ -> 흰방 : 가중치 1
"""