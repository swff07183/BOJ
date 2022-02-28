import sys
sys.stdin = open("input.txt")

N, K = map(int, input().split())
arr = list(map(int, input().split()))
max_t = 0
for i in range(N-K+1):
    total = 0
    for j in range(i, i+K):
        total += arr[j]

    if max_t < total:
        max_t = total

print(max_t)