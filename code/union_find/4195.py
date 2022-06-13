import sys
input = lambda: sys.stdin.readline().rstrip()

def find_(name):
    if par[name] != name:
        par[name] = find_(par[name])
    return par[name]

def union_(a, b):
    a = find_(a)
    b = find_(b)
    if a == b:
        sz = size[a]
    elif rank[a] > rank[b]:
        par[b] = a
        size[a] += size[b]
        sz = size[a]
    else:
        par[a] = b
        size[b] += size[a]
        if rank[a]==rank[b]:
            rank[b] += 1 
        sz = size[b]
    return sz

T = int(input())
for tc in range(T):
    F = int(input())
    par = {}
    size = {}
    rank = {}
    for _ in range(F):
        a, b = input().split()
        if not par.get(a):
            par[a] = a
            size[a] = 1
            rank[a] = 1
        if not par.get(b):
            par[b] = b
            size[b] = 1
            rank[b] = 1
        sz = union_(a, b)
        print(sz)