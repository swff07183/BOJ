import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
arr = sorted([int(input()) for _ in range(N)])
result = int(1e10)

# 이번 문제는 두 수의 차이 구하는거니까
# l, r 둘다 0에서 시작했따
l, r = 0, 0
while l <= N-1 and r <= N-1:
    tmp = arr[r] - arr[l]           # 차이 저장해주고
    if tmp >= M:                    # M 이상이면서
        result = min(result, tmp)   # 최소값인 차이 찾아주고
    if tmp > M:                     # 차이가 M보다 크면 더 작아져야 하니 l 증가
        l += 1
    else:                           # 아니면 r 증가
        r += 1 
print(result)