N = int(input())
a = sorted(list(map(int, input().split())))
x = int(input())

l = 0
r = N-1
cnt = 0
while l < r:
    tmp = a[l] + a[r]
    if tmp == x:
        cnt += 1
        l += 1
        r -= 1
    elif tmp > x:
        r -= 1
    else:
        l += 1
print(cnt)