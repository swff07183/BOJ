# 2252 줄세우기
import sys
input = lambda : sys.stdin.readline().rstrip()
from collections import deque

def topology():
    queue = deque()
    result = []

    for i in range(1, N+1):
        if indegree[i] == 0:        # 진입차수가 0이면 
            queue.append(i)         # queue에 넣어주기

    while queue:                    # queue에 노드가 남아있으면
        node = queue.popleft()      # 맨 앞에 있는거 pop
        result.append(node)         # result에 추가해주기
        for nxt in graph[node]:     # 해당 노드에서 갈수있는곳 탐색해서
            indegree[nxt] -= 1      # 진입차수 제거
            if indegree[nxt] == 0:  # 진입차수가 0이면
                queue.append(nxt)   # queue에 nxt 추가
                
    return result

N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]        # 그래프
indegree = [0 for _ in range(N+1)]      # 진입 차수

for _ in range(M):
    a, b = map(int, input().split())    # a -> b
    graph[a].append(b)                  # 그래프 만들어주고
    indegree[b] += 1                    # b의 진입차수 1 증가
result = topology()                     # 위상정렬 결과
print(*result)