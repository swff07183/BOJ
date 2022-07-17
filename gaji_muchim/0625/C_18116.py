"""
18116 로봇조립
-> 유니온 파인드 문제
I 일때는 두 집합 합치기
Q 일때는 해당 집합의 size 확인하기
"""

import sys
input = lambda : sys.stdin.readline().rstrip()

MAX_RANGE = int(1e6) + 1

def union_(x, y):
    x = find_(x)
    y = find_(y)
    if x == y:
        return
    elif x > y:
        par[x] = y
        size[y] += size[x]
    else:
        par[y] = x
        size[x] += size[y]

def find_(x):
    if x != par[x]:
        par[x] = find_(par[x])
    return par[x]


N = int(input())

par = [x for x in range(MAX_RANGE)]
size = [1 for x in range(MAX_RANGE)]

for _ in range(N):
    oper = input().split()
    if oper[0] == 'I':
        a, b = map(int, oper[1:])
        union_(a, b)
    elif oper[0] == 'Q':
        c = find_(int(oper[1]))
        print(size[c])
