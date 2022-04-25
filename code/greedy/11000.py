import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort()

q = []
heapq.heappush(q, arr[0][1])
for s, t in arr[1:]:
    if s >= q[0]:
        heapq.heappop(q)
        heapq.heappush(q, t)
    else:
        heapq.heappush(q, t)

print(len(q))