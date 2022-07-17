"""
서강그라운드
플로이드 와샬 돌려서 모든 정점 사이의 최단 거리 구함
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

INF = int(1e9)

n, m, r = map(int, input().split())

arr = [0] + list(map(int, input().split()))

dist = [[INF for _ in range(n+1)] for _ in range(n+1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    dist[a][b] = l
    dist[b][a] = l


for i in range(1, n+1):
    dist[i][i] = 0

# 플-와
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            new_d = dist[i][k] + dist[k][j]
            dist[i][j] = min(dist[i][j], new_d)

ans = 0

# 1~n 까지 탐색하면서 한 점에서 출발했을때 값 계산해서 최고값 찾기
for i in range(1, n+1):
    tmp = 0
    for j in range(1, n+1):
        if dist[i][j] <= m:
            tmp += arr[j]
    ans = max(ans, tmp)
print(ans)