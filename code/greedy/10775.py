import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def find_(x):
    if par[x] == x:
        return x
    else:
        par[x] = find_(par[x])
        return par[x]

def union_(x, y):
    x = find_(x)
    y = find_(y)
    if x==y:
        return
    elif x > y:
        par[x] = y
    else:
        par[y] = x



G = int(input())
P = int(input())
par = [x for x in range(G+1)]
result = 0
for _ in range(P):
    gi = int(input())
    x = find_(gi)
    if x == 0:
        break
    union_(x, x-1)
    result += 1
print(result)