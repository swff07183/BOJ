import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input().rstrip())
    arr = [tuple(map(int, input().split())) for _ in range(N)]

    # 서류 기준 오름차순정렬
    arr.sort(key=lambda x:x[0])
    cnt = 0
    tmp = arr[0][1]
    for s in arr:
        if s[1] <= tmp:
           cnt += 1
           tmp = s[1]

    print(cnt)