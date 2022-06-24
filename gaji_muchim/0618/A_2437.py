import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = sorted(list(map(int, input().split())))


tmp = 0
for num in arr:
    if tmp+1 < num:
        result = tmp+1
        print(result)
        exit()
    tmp += num

print(tmp+1)


"""
7
3 1 6 2 7 30 1
-> 정렬
1 1 2 3 6  7  30

1 2 4 7 13 20 50
"""