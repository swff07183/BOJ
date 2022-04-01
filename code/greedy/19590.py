import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]

max_num = max(arr)
bead_sum = sum(arr) - max_num
result = max_num - bead_sum
if result > 0:
    print(result)
else:
    print(1 if result%2 else 0)