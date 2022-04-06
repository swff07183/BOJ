import sys
sys.stdin = open('input.txt')

def find_(x):
    if p[x] == x:
        return x
    else:
        p[x] = find_(p[x])
        return p[x]

def union(x, y):
    x = p[x]
    y = p[y]
    if x == y:
        return
    elif x > y:
        p[x] = y
    else:
        p[y] = x

def check_plan(*args):
    parent = find_(args[0])
    for i in range(1, M):
        if find_(args[i]) != parent:
            return "NO"
    else:
        return "YES"

N = int(input())
M = int(input())

p = [x for x in range(N+1)]
for i in range(N):
    data = list(map(int, input().split()))
    for j in range(N):
        if data[j]:
            union(i+1, j+1)
plan = list(map(int, input().split()))
print(check_plan(*plan))