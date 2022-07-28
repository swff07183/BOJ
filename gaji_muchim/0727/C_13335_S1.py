"""
트럭
마지막 친구가 어느 시점에 들어갈 수 있는지만 구하면 된다.
"""
import sys
sys.stdin = open('input.txt')
from collections import deque

n, w, L = map(int, input().split())
arr = list(map(int, input().split()))
start, tmp, ans = 0, 0, 0
queue = deque()
for i in range(n):
    while tmp+arr[i] > L:
        weight, time = queue.popleft()
        tmp -= weight
        start = (time + w)
    while queue and queue[0][1] + w <= start:
        tmp -= queue.popleft()[0]
    queue.append((arr[i], start))
    ans = (start + w + 1)
    tmp += arr[i]
    start += 1
print(ans)