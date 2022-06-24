import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = [int(input()) for _ in range(N)]

result = 0

for i in range(len(arr)-2, -1, -1): # 뒤에서부터 순회하면서
    if arr[i] >= arr[i+1]:          # 앞의 숫자가 더 크거나 같다면
        tmp = arr[i+1] - 1          # 뒤의숫자 -1 로 만들어주기
        result += (arr[i] - tmp)
        arr[i] = tmp
print(result)