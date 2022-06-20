import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])
result = int(1e10)

l, r = 0, 0
while l <= N-1 and r <= N-1:
    tmp = arr[r] - arr[l]
    if tmp >= M:
        result = min(result, tmp)
    if tmp > M:
        l += 1
    else:
        r += 1
print(result)