N = int(input())
A = list(map(int, input().split()))

# cnt_l = [0 for _ in range(1001)]
# cnt_r = [0 for _ in range(1001)]
# l = [0 for _ in range(N)]
# r = [0 for _ in range(N)]

# for i in range(N):
#     num = A[i]
#     cnt_l[num] = max(cnt_l[:num]) + 1
#     l[i] = cnt_l[num]

# for j in range(N-1, -1, -1):
#     num = A[j]
#     cnt_r[num] = max(cnt_r[:num]) + 1
#     r[j] = cnt_r[num]

dp_l = [1 for _ in range(N)]
dp_r = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            dp_l[i] = max(dp_l[i], dp_l[j] + 1)

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j]:
            dp_r[i] = max(dp_r[i], dp_r[j] + 1)

print(A)
print(dp_l)
print(dp_r)
result = 0

for i in range(N):
    total = dp_l[i] + dp_r[i] - 1
    if total > result:
        result = total

print(result)
