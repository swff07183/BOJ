import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().rstrip().split()))

s, e = 0, 0
cnt = 0
result = 0
while s < N and e < N:
    print(arr[s:e+1])
    if arr[e] % 2 != 0:
        cnt += 1
    if cnt > K:
        while s < e:
            if arr[s] % 2 != 0:
                s += 1
                cnt -= 1
                break
            s += 1
    result = max(result, e-s-cnt+1)
    e += 1

print(result)