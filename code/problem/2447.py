import sys
sys.stdin = open("input.txt")


N = int(input())
arr = []
for _ in range(6):
    _, l = map(int, input().split())
    arr.append(l)

max_idx = arr.index(max(arr))

area = 0
for i in [1, 4]:
    x = (max_idx + i) % 6
    y = (max_idx + i+1) % 6
    area += arr[x] * arr[y]
print(area * N)