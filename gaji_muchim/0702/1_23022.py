"""
현재 할 수 있는것중에, 단위시간당 벌점 최대인 숙제 하기
왜? 하나 실행하면 [나머지 벌점의 합] 만큼 벌점 올라간다.
    -> 그래서 [나머지 벌점의 합] 이 최소가 되도록

"""

import sys, heapq

T = int(input())
for _ in range(T):
    n, S = map(int, input().split())
    t = list(map(int, input().split()))
    v = list(map(int, input().split()))

    data = []
    for i in range(n):
        data.append([t[i], -v[i]])          # [시간, 벌점] 으로 리스트 넣기
    data.sort(reverse=True)                 # 시간 느린 순으로 정렬

    ans = 0                                 # 현재까지 받은 벌점
    queue = []                              # 우선순위 큐 -> 현재 실행할 수 있는 녀석들
    while data and data[-1][0] <= S:        # S보다 작은 것들 큐에 넣기
        time, score = data.pop()
        heapq.heappush(queue, [score, time])
    while queue:
        score, time = heapq.heappop(queue)  # 현재 실행할 수 있는 것중에 벌점이 가장 큰거 빼서
        ans += (S-time) * score             # 점수 저장
        S += 1                              # 시간 1 증가 시켰는데
        if data and not queue:              # 만약에 queue에 아무것도없다면
            S = data[-1][0]                 # 가장 빨리 실행할 수 있는 시간으로 S 바꾸기
        while data and data[-1][0] <= S:    # S보다 작은 것들 다 추가하기
            time, score = data.pop()
            heapq.heappush(queue, [score, time])
    print(-ans)



# import sys, heapq

# T = int(input())
# for _ in range(T):
#     n, S = map(int, input().split())
#     t = list(map(int, input().split()))
#     v = list(map(int, input().split()))

#     data = []
#     for i in range(n):
#         data.append([t[i], -v[i]])          # [시간, 벌점] 으로 리스트 넣기
#     data.sort()                             # 시간 빠른 순으로 정렬

#     ans = 0                                 # 현재까지 받은 벌점
#     queue = []                              # 우선순위 큐 -> 현재 실행할 수 있는 녀석들
#     i = 0                                   # 탐색할 인덱스
#     while i < n and data[i][0] <= S:        # S보다 작은 것들 큐에 넣기
#         heapq.heappush(queue, [data[i][1], data[i][0]])
#         i += 1
#     while queue:
#         score, time = heapq.heappop(queue)  # 현재 실행할 수 있는 것중에 벌점이 가장 큰거 빼서
#         ans += (S-time) * score             # 점수 저장
#         S += 1                              # 시간 1 증가 시켰는데
#         if i < n and not queue:             # 만약에 queue에 아무것도없다면
#             S = data[i][0]                  # 가장 빨리 실행할 수 있는 시간으로 S 바꾸기
#         while i < n and data[i][0] <= S:    # S보다 작은 것들 다 추가하기
#             heapq.heappush(queue, [data[i][1], data[i][0]])
#             i += 1
#     print(-ans)