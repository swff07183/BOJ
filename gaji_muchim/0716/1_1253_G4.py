"""
좋다
N <= 2000인데 그냥 두개의 수 합 모두 더해놓으면 안되나?
그래서 그냥 정렬하고 이분탐색 하면 될거같은데
-> 근데 틀림 진짜 맞는데 왜틀림?

반례 :
6
0 0 3 3 3 3
답: 4

-> 어떤 수가 다른 두 수의 합으로 나타내야 한다. 위의 로직으로는 불가능.
걍 투포인터 ㄱ
근데 정렬 안해서 한번 더 틀림
"""
import sys
sys.stdin = open('input.txt')
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = list(map(int, input().split()))
arr.sort()              # 투포인터 돌릴꺼니까 정렬!

ans = 0                 # 답 개수
for i in range(N):      # 모든 숫자에 대해 투포인터 고
    target = arr[i]     # arr[i] 찾기
    s = 0               # 처음부터
    e = N-1             # 끝까지인데
    while s < e:
        if s == i:      # i는 합에 포함되면 안된다
            s += 1
            continue
        elif e == i:
            e -= 1
            continue
        tmp = arr[s]+arr[e] # 그래서 합 구해주고
        if tmp == target:   # 좋은수면
            ans += 1        # 값 증가
            break
        elif tmp < target:
            s += 1
        else:
            e -= 1
print(ans)



# def get_sum(cur, s, total):
#     if cur == 2:
#         two_sum.append(total)
#         return
#     for i in range(s, N):
#         get_sum(cur+1, i+1, total+arr[i])

# def is_good(target):
#     s = 0
#     e = len(two_sum)
#     while s <= e:
#         mid = (s+e) // 2
#         if two_sum[mid] == target:
#             return True
#         if target > two_sum[mid]:
#             s = mid + 1
#         else:
#             e = mid - 1
#     return False

# N = int(input())
# arr = list(map(int, input().split()))

# two_sum = [] # 두개의 수 합
# get_sum(0, 0, 0)
# two_sum.sort()
# ans = 0
# for i in range(N):
#     if is_good(arr[i]):
#         ans += 1

# print(ans)