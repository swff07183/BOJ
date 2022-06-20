import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = [int(input()) for _ in range(N)]

result = 0
for i in range(len(arr)-2, -1, -1):
    if arr[i] >= arr[i+1]:
        tmp = arr[i+1] - 1
        result += (arr[i] - tmp)
        arr[i] = tmp
print(result)