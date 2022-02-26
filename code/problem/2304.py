import sys
sys.stdin = open("input.txt")

N = int(input())
arr = []
for i in range(N):
    arr.append(tuple(map(int, input().split())))

arr.sort()

last_l, last_h = arr[0]
total = 0


i = 1
while True:
    """
    기둥 높이 증가 -> 너비 바로 구하기
    기둥 높이 감소 ->
    """
    l, h = arr[i]
    if last_h <= h:  # 증가하는 경우
        area = (l - last_l) * last_h
        total += area
        last_l, last_h = l, h
        i += 1
    elif last_h > h:  # 감소하는 경우
        check_h = last_h
        while i < len(arr) and arr[i][1] < check_h:
            check_h = arr[i][1]
            i += 1

    if i >= len(arr):
        total += last_h
        l, h = arr[-1]
        area = (l - last_l) * h
        total += area
        break


print(total)
