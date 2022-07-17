"""
아기상어2
"""
import sys
sys.stdin = open('input.txt')
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def bfs(si, sj):
    queue = deque()
    visited = [[False for _ in range(M)] for _ in range(N)]
    queue.append([si, sj])
    visited[si][sj] = True

    ans = 0  # 안전거리
    while queue:
        for _ in range(len(queue)): # 안에는 거리가 ans인 녀석들 들어가있음
            i, j = queue.popleft()
            if arr[i][j]:
                return ans
            for d in range(8):
                ni = i + di[d]
                nj = j + dj[d]
                if not (0<=ni<N and 0<=nj<M) or visited[ni][nj]:
                    continue
                visited[ni][nj] = True
                queue.append([ni, nj])
        ans += 1
        

di = [-1, -1, -1, 0, 0, 1, 1, 1]
dj = [0, -1, 1, -1, 1, 0, -1, 1]


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0  # 안전거리 최대값

# 모든 점에 대해서 안전거리 확인하면서 최대값 갱신
for i in range(N):
    for j in range(M):
        ans = max(ans, bfs(i, j))   

print(ans)