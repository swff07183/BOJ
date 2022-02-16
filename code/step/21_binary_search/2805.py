# pypy
import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))

woods = list(map(int, input().split()))

start = 0
end = max(woods)

while start <= end:
    mid = (start + end) // 2

    total = 0
    for wood in woods:
        if wood > mid:
            cut = wood - mid
            total += cut

    if total >= M:
        start = mid + 1
    else :
        end = mid - 1
print(end)