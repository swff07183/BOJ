import sys, heapq
input = sys.stdin.readline

def get_dist(a, b):
    x = a[0] - b[0]
    y = a[1] - b[1]
    return (x**2 + y**2) ** 0.5

def find_(x):
    if p[x] == x:
        return x
    else:
        p[x] = find_(p[x])
        return p[x]

def union_(x, y):
    x = find_(x)
    y = find_(y)
    if x < y:
        p[y] = x
    else:
        p[x] = y

N, M = map(int, input().split())
p = [i for i in range(N+1)]
arr = [(0, 0)]


for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

for _ in range(M):
    a, b = map(int, input().split())
    union_(a, b)

result = 0
data = []
for i in range(1, N+1):
    for j in range(i+1, N+1):
        data.append([get_dist(arr[i], arr[j]), i, j])
data.sort()
for d, a, b in data:
    if find_(a) != find_(b):
        result += d
        union_(a, b)
        
print(f"{result:.2f}")