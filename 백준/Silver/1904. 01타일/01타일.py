import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline        

N = int(input())

arr = [0 for _ in range(N+2)]
arr[0] = 1
arr[1] = 1

for i in range(2, N+1):
    arr[i] = (arr[i-1] + arr[i-2]) % 15746
print(arr[N])