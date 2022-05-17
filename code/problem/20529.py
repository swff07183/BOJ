import sys
input = sys.stdin.readline
from itertools import combinations

def distance(a, b):
    ret = 0
    for i in range(4):
        if a[i] != b[i]:
            ret += 1
    return ret

T = int(input())

for tc in range(T):
    N = int(input())

    arr = input().split()
    if N >= 33:
        print(0)
        continue
    
    result = 999
    pick = list(combinations(arr, 3))

    for a, b, c in pick:
        tmp = 0
        tmp += distance(a, b)
        tmp += distance(b, c)
        tmp += distance(c, a)
        result = min(result, tmp)
    
    print(result)