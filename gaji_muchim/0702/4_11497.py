"""
최소 난이도가 되는 경우

ex) 통나무가 9개 일때
배열 정렬한 인덱스 0~8 일때
[0, 2, 4, 6, 8] + [7, 5, 3, 1]
이때 인접한 두개 차이 중 가장 큰 값 구해주자.
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    arr = [arr[i] for i in range(0, N, 2)] + [arr[j] for j in range(1, N, 2)][::-1]
    arr.append(arr[0])

    ans = 0
    for i in range(N):
        ans = max(ans, abs(arr[i] - arr[i-1]))
    
    print(ans)