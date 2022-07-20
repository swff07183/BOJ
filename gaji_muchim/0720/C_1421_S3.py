"""
나무꾼 이다솜
N <= 50
나무 길이 <= 10,000
500,000 -> 완탐 ㄱ

처음에 틀림
안파는게 좋은 경우도 있다..
"""
N, C, W = map(int, input().split())
arr = [int(input()) for _ in range(N)]

max_len = max(arr)  # 최대 길이 저장

ans = 0
for l in range(1, max_len+1):       # 모든 경우의 수 보면서
    total = 0                       # l로 잘랐을 때 벌 수 있는 돈
    for i in range(N):              # 나무 하나씩 확인해서
        if l > arr[i]:              # 못자르면 패쓰
            continue
        cut = arr[i]//l if arr[i]%l else arr[i]//l-1    # 자르는 횟수
        total += max(0, W*l*(arr[i]//l) - cut*C)        # 가격 구해서 더해주기

    ans = max(total, ans)
    
print(ans)