import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())
max_b = 0
result = 0

arr = [tuple(map(int, input().split())) for _ in range(N)]

arr.sort()
for i in range(N):
    tmp = 0
    for j in range(i, N):
        tmp += max(0, arr[i][0] - arr[j][1])
    if tmp > max_b:
        max_b = tmp
        result = arr[i][0]

print(result)