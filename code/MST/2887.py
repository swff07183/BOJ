import sys
input = lambda: sys.stdin.readline().rstrip()

def union_(x, y):
    x = find_(x)
    y = find_(y)
    if x > y:
        p[x] = y
    else:
        p[y] = x

def find_(x):
    if p[x] != x:
        p[x] = find_(p[x])
    return p[x]
    

N = int(input())
p = [x for x in range(N+1)]

# [node, x, y, z]
arr = [[node] + list(map(int, input().split())) for node in range(1, N+1)]

data = []
for i in range(1, 4):
    arr.sort(key=lambda x:x[i])
    for j in range(N-1):
        data.append([abs(arr[j][i] - arr[j+1][i]), arr[j][0], arr[j+1][0]])
data.sort(key=lambda x:x[0])

V = 0
result = 0
for d, a, b in data:
    if find_(a) != find_(b):
        union_(a, b)
        V += 1
        result += d

print(result)