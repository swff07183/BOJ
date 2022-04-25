import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))
tmp = sum(arr[0:K])
result = tmp
s = 0
e = K-1

while e < N-1:
    tmp -= arr[s]
    s += 1
    e += 1
    tmp += arr[e]
    result = max(tmp, result)
print(result)