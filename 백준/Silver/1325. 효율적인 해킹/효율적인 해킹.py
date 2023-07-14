import sys
input = sys.stdin.readline

from collections import deque

def bfs(start):
    queue = deque()
    queue.append(start)
    v = [False for _ in range(N+1)]
    v[start] = True
    cnt = 1
    while queue:
        com = queue.popleft()
        for next_com in arr[com]:
            if not v[next_com]:
                v[next_com] = 1
                cnt += 1
                queue.append(next_com)
    return cnt

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    # arr[a].append(b) 
    arr[b].append(a)

result = []
max_com = 0

for i in range(1, N+1):
    coms = bfs(i)
    if coms > max_com:
        max_com = coms
        result = [i]
    elif coms == max_com:
        result.append(i)
print(*result)