import sys, heapq
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

def solve_problems():
    result = []
    q = []
    for i in range(1, N+1):
        if indegree[i] == 0:
            heapq.heappush(q, i)
    while q:
        node = heapq.heappop(q)
        result.append(node)
        while arr[node]:
            nxt = heapq.heappop(arr[node])
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                heapq.heappush(q, nxt)
    
    return result

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
indegree = [0 for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    heapq.heappush(arr[a], b)
    indegree[b] += 1

result = solve_problems()
print(*result)