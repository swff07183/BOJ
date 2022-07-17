"""
S 길이 최대 10 -> 걍 완탐 ㄱ
다 해서 행운문자열인거 
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def is_lucky(word):
    for i in range(N-1):
        if word[i] == word[i+1]:
            return False
    return True

def rearr(cnt, tmp):
    global ans
    if cnt == N:
        if is_lucky(tmp):
            ans.append(tmp)
        return
    for i in range(N):
        if not v[i]:
            v[i] = True
            rearr(cnt+1, tmp+word[i])
            v[i] = False

word = input()
N = len(word)
v = [False for _ in range(N)]

ans = []
rearr(0, '')
print(len(set(ans)))