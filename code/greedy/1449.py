import sys
input = sys.stdin.readline

N, L = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()
v = [False for _ in range(1001)]

cnt = 0

for c in arr:
    if not v[c]:
        v[c:c+L] = [True]*L
        cnt += 1
print(cnt)
    