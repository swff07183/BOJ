"""
-1, +1 해서 누적합으로 풀어볼까 하다가
T 범위 21억 -> 배열 만들면 절때 불가능
그럼 딕셔너리 ㄱ?
-> 출입이 있는 시간만 확인한다
n 최대 1,000,000. O(n)에 가능
"""

import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())

T_dict = {}

for _ in range(N):
    e, x = map(int, input().split())
    T_dict[e] = T_dict.get(e, 0) + 1    # 모기 들어온 시간
    T_dict[x] = T_dict.get(x, 0) - 1    # 모기 나온 시간

arr = sorted(T_dict.items())            # 시간 순 정렬

tmp = 0
ans = 0
s, e = 0, 0
isRecord = False

for t, c in arr:
    tmp += c                        # 누적합 기록해주고
    if ans < tmp:                   # 최대 모기면
        ans = tmp                   # 최대 
        s = t                       # 시작 시간 기록
        isRecord = True             # 최대값 기록중
    elif isRecord and ans > tmp:    # 최대값 기록중이고 시간 줄어들었다
        e = t                       # 마치는 시간 기록
        isRecord = False            # 기록 끝
print(ans)
print(s, e)