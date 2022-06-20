# 2110 공유기 설치
import sys
input = lambda : sys.stdin.readline().rstrip()

def bin_search():
    """
    이분 탐색
    가장 인접한 공유기의 거리
    """
    s = 1           # 최소 거리 : 1
    e = arr[-1] - 1 # 최대 거리 : 가장 멀리있는거 - 1

    while s <= e:
        mid = (s + e) // 2
        tmp = arr[0]                # 무조건 첫번째 집에 설치하기
        cnt = 1                     # 공유기 개수 1부터 시작

        for i in range(1, N):
            if arr[i]-tmp >= mid:   # 설치할 수 있는 거리면
                cnt += 1            # 개수 증가시키고
                tmp = arr[i]        # 이전 위치 저장

        if cnt >= C:                # 개수가 C보다 크거나 많다
            s = mid + 1             # 거리 늘려서 다시 탐색
        else:
            e = mid - 1             # 적으면 거리 줄여서 다시 탐색
            
    return e        
    

N, C = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()              # 이분탐색 위해 정렬하기
result = bin_search()   # 결과 저장    
print(result)