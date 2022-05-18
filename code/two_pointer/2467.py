N = int(input())
arr = list(map(int, input().split()))
arr.sort()

s, e = 0, N-1
x = arr[0]
y = arr[N-1]

while s < e:
    if abs(arr[s]+arr[e]) < abs(x + y):
        x = arr[s]
        y = arr[e]
    tmp = arr[s] + arr[e]
    if tmp < 0:
        s += 1
    else:
        e -= 1

print(x, y)

