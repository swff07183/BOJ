"""
접두사
길이 긴거 순으로 정렬하고
하나씩 순회 하면서 ans에 하나씩 넣을꺼다
넣는 조건 -> 현재 확인 중인 단어가 ans에 들어가있는 모든 단어의 접두사가 아니면
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())

arr = [input() for _ in range(N)]

arr.sort(key=lambda x: -len(x))

ans = []

for pref in arr:
    for word in ans:
        if word[:len(pref)] == pref:
            break
    else:
        ans.append(pref)

print(len(ans))