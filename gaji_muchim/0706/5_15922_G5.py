"""
지난번 모기쓰랑 비슷하게 풀었음
딕셔너리 사용해서 +1, -1 기록해줬고
값이 양수인 구간의 길이 구했다
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
check = {}
for _ in range(N):
    x, y = map(int, input().split())

    check[x] = check.get(x, 0) + 1
    check[y] = check.get(y, 0) - 1

check = sorted(check.items(), key=lambda x: x[0])
tmp = 0
ans = 0
isRecord = False
s = int(1e10)
for x, c in check:
    tmp += c
    if tmp > 0 and not isRecord:
        isRecord = True
        s = x
    elif tmp <= 0 and isRecord:
        isRecord = False
        ans += (x - s)
print(ans)