import sys
sys.stdin = open("input.txt")

N = int(input())
arr = [0 for _ in range(1001)]

start, end = 1001, -1

for i in range(N):
    l, h = map(int, input().split())
    arr[l] = h
    if l < start:
        start = l
    if l > end:
        end = l
max_idx = arr.index(max(arr))
"""
start : 시작
max_idx : 최고점
end : 끝 좌표
"""
last_h = 0
for i in range(start, max_idx):
    if last_h < arr[i]:
        last_h = arr[i]
    else:
        arr[i] = last_h
last_h = 0
for i in range(end, max_idx, -1):
    if last_h < arr[i]:
        last_h = arr[i]
    else:
        arr[i] = last_h

print(sum(arr[start:end+1]))