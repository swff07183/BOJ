import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().split()))
result = [-1 for _ in range(N)]

sorted_arr = sorted(list(enumerate(arr)), key=lambda x:x[1])

for i in range(N):
    result[sorted_arr[i][0]] = i

print(*result)