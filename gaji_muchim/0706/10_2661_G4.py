"""
수열 만들었다.
완탐하면 3^80가지 경우
-> 가지치기 해야함
그냥 check 함수 만들어서 dfs 들어갈때마다 해줬음
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

def check(seq):
    for i in range(1, len(seq)+1):
        for j in range(len(seq)-(i*2)+1):
            if seq[j:j+i]==seq[j+i: j+i+i]:
                return False
    return True

def dfs(cnt, tmp, prv=-1):
    if not check(tmp):
        return
    if cnt == N:
        if check(tmp):
            print(tmp)
            exit()
        return
    for i in range(3):
        if prv==i:
            continue
        dfs(cnt+1, tmp + arr[i], i)


N = int(input())
arr = ['1', '2', '3']
dfs(0, '')