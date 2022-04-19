import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, K = map(int, input().split())

jew = [tuple(map(int, input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]

jew.sort()
bags.sort()

tmp = []
result = 0

for bag in bags:
    # 가방 무게보다 적은 보석들 가격 최대 힙에 넣기
    while jew and jew[0][0] <= bag:
        heapq.heappush(tmp, -heapq.heappop(jew)[1])
    # 만약 넣을수 있는 보석이 있다면
    if tmp:
        result += -heapq.heappop(tmp)
    # 더이상 넣을 수 있는 보석이 없다면
    elif not jew:
        break

print(result)