N, M = map(int, input().split())

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

p = [i for i in range(N+1)]

for i in range(1, M+1):
    a, b = map(int, input().split())
    a = find_(a)
    b = find_(b)
    if a == b:
        print(i)
        exit(0)
    union_(a, b)
print(0)