"""
위상정렬 + DP
이전에 한번 비슷한 문제 풀어서 금방 풀었던거 같다.
똑같이 위상정렬 해주고,
부모 중 가장 늦게 끝난거 + 해당 작업 완료하는데 걸린시간
"""
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

def topology():
    queue = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:        # 초기 진입차수 0인것들
            dp[i] = time[i]         # 시간 기록해주고
            queue.append(i)         # queue에 추가
    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            indegree[nxt] -= 1      # 진입차수 1 빼주기
            if indegree[nxt] == 0:  # 차수 0이면 큐에 추가
                queue.append(nxt)
            dp[nxt] = max(dp[nxt], dp[node] + time[nxt])    # 현재까지 시간, 이번 작업까지 시간 중 최대값 기록

N = int(input())
time = [0 for _ in range(N+1)]      # 해당 작업을하는데 걸리는 시간
graph = [[] for _ in range(N+1)]    # 그래프
indegree = [0 for _ in range(N+1)]  # 진입 차수
dp = [0 for _ in range(N+1)]        # 작업 완료하기까지 걸리는 시간
for i in range(1, N+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    indegree[i] = data[1]
    for j in range(2, 2 + data[1]):
        graph[data[j]].append(i)

topology()

print(max(dp))