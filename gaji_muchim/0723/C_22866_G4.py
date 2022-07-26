"""
탑 보기
8
3 7 1 6 3 5 1 7
"""

import sys
sys.stdin = open('input.txt')
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = [0] + list(map(int, input().split()))
ans = [0 for _ in range(N+1)]
cnt = [0 for _ in range(N+1)]


left = []

for i in range(1, N+1):
    while left and arr[left[-1]] <= arr[i]:
        left.pop()
    if not left:
        left.append(i)
        continue
    ans[i] = left[-1]
    cnt[i] += len(left)
    left.append(i)

right = []
for j in range(N, 0, -1):
    while right and arr[right[-1]] <= arr[j]:
        right.pop()
    if not right:
        right.append(j)
        continue
    if ans[j] == 0 or abs(j - ans[j]) > abs(j - right[-1]):
        ans[j] = right[-1]
    cnt[j] += len(right)
    right.append(j)

for i in range(1, N+1):
    if not cnt[i]:
        print(0)
    else:
        print(cnt[i], ans[i])