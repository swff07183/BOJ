import sys
input = lambda : sys.stdin.readline().rstrip()

N = int(input())
arr = sorted(list(map(int, input().split())))

l, r = 0, N-1       # 시작, 끝 인덱스 설정
min_v = int(1e10)   # 최소값 저장할 변수
result = [0, 0]     # 결과 저장할 두 변수. 그냥 0, 0으로

while l < r:
    tmp = arr[l] + arr[r]           # 특성값 저장
    if abs(tmp) < min_v:            # 0에 더 가까우면 -> 절대값이 더 작으면
        min_v = abs(tmp)            # 최소값 갱신하고
        result = [arr[l], arr[r]]   # 결과 담아두기
    if tmp <= 0:                    # 특성값이 음수면 더 커져야 하니
        l += 1                      # l 증가
    else:                           # 특성값이 양수면 더 작아져야 하니
        r -= 1                      # r 감소

print(*result)





"""
처음에 l <= r 로 했다가 틀렸다..

반례 :
5
1 2 3 4 5

당연히 틀렸지. 같은 용액 두번 못고르니까..!
"""