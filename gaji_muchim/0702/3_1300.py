"""
B[k] 구해야 한다..
N*N 배열에서 특정 숫자 x의 인덱스 구하기 위해서..
i번째 행에서 x보다 작거나 같은 숫자의 개수 -> min(N, x//i)가 된다.
요렇게 해서 작거나 같은 숫자의 개수 cnt 세주고 -> 요게 이분탐색 매개변수
cnt >= k 라면 B[k]가 x보다 작을수 있으니 e = mid - 1
cnt < k 라면 B[k]가 x보다 커야 하니 s = mid + 1

1 2 3 4 5 6 7 8 9 10
2 4 6 8 10 12 14 16 18 20
3 6 9 12 15 18 21 24 27 30
4 8 12 16 20 24 28 32 36 40
5 10 15 20 25 30 35 40 45 50
6 12 18 24 30 36 42 48 54 60
7 14 21 28 35 42 49 56 63 70
8 16 24 32 40 48 56 64 72 80
9 18 27 36 45 54 63 72 81 90
10 20 30 40 50 60 70 80 90 100
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
k = int(input())

def bin_search():
    s = 1
    e = N*N

    while s <= e:
        mid = (s + e) // 2
        cnt = 0
        for i in range(1, N+1):
            cnt += min(mid // i, N)
        if cnt >= k:
            e = mid - 1
        else:
            s = mid + 1
    
    return s

ans = bin_search()
print(ans)