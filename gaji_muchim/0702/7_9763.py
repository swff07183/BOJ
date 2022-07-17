"""
10번 틀렸다.
시간초과 4회
틀렸습니다 4회
메모리초과 2회

처음 생각한거
그냥 두개 사이 거리 구해서 O(N^2)
그거 중에 최소값 두개 더하면 되지 않나?
-> 어림도 없음. (1-2, 3-4) 이런 경우도 있기 때문에

12 23

그래서 하나 고정 시키고(i: 0~N)
나머지 탐색하면서(j:0~N)
거기서 최소값, 두번째 작은값 구함.
그거 두개 더한다음 여태까지 최소값이랑 비교해서 갱신
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

def dist(p1, p2):
    # 두 점 사이 거리
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + abs(p1[2]-p2[2])

N = int(input())

arr = []

for _ in range(N):
    x, y, z = map(int, input().split())
    arr.append([x, y, z])

ans = int(1e9)

for i in range(N):
    min1 = int(1e9)                 # 최소값
    min2 = int(1e9)                 # 두번째로 작은 값
    for j in range(N):
        if i == j:
            continue
        d = dist(arr[i], arr[j])    # i, j 거리 구하고
        if d <= min1:               # d가 최소값이라면
            min2 = min1             # 두번째로 작은값은 min1이 되고
            min1 = d                # 최소값은 d가 된다
        elif d <= min2:             # d가 min1~min2 사이 라면
            min2 = d                # min2만 갱신
    ans = min(ans, min1 + min2)

print(ans)