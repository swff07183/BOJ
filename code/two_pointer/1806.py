import sys
input = sys.stdin.readline

N, S = map(int, input().split())

arr = list(map(int, input().split()))

i = 0
j = 0
total = arr[0]
result = N+1

while True:
    if total < S:
        j += 1
        if j >= N:
            break
        total += arr[j]
    else:
        result = min(result, j-i+1)
        total -= arr[i]
        i += 1

if result == N+1:
    print(0)
else:
    print(result)