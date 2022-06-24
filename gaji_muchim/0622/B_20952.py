import sys
input = lambda: sys.stdin.readline().rstrip()

DIV_NUM = int(1e9) + 7

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

div_a = [0 for _ in range(7)]

for i in range(N):
    div_a[A[i] % 7] += 1

is_zero = [False for _ in range(7)]
plus = 0

for i in range(M):
    cnt, zero_cnt = 0, 0
    plus_tmp = plus + B[i]
    tmp = is_zero[:]
    for j in range(7):
        if is_zero[j] or not div_a[j]:
            continue
        cnt += div_a[j]
        if (j + plus_tmp) % 7 == 0:
            zero_cnt += div_a[j]
            tmp[j] = True
    if zero_cnt != cnt:
        is_zero = tmp[:]
        plus = plus_tmp

result = []

for i in range(N):
    if is_zero[A[i] % 7]:
        continue
    result.append((A[i] + plus) % DIV_NUM)

print(len(result))
print(*result)