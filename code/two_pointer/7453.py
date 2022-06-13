import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
arr_A = []
arr_B = []
arr_C = []
arr_D = []
for _ in range(n):
    na, nb, nc, nd = map(int, input().split())
    arr_A.append(na)
    arr_B.append(nb)
    arr_C.append(nc)
    arr_D.append(nd)

arr_sum1 = []
arr_sum2 = []

for i in range(n):
    for j in range(n):
        arr_sum1.append(arr_A[i] + arr_B[j])
        arr_sum2.append(arr_C[i] + arr_D[j])

arr_sum1.sort()
arr_sum2.sort(reverse=True)
l, r = 0, 0
result = 0
while l<len(arr_sum1) and r<len(arr_sum2):
    tmp = arr_sum1[l] + arr_sum2[r]
    if tmp == 0:
        tmp1, tmp2 = arr_sum1[l], arr_sum2[r]
        c1, c2 = 1, 1
        l += 1
        r += 1
        while l < len(arr_sum1) and arr_sum1[l]==tmp1:
            l += 1
            c1 += 1
        while r < len(arr_sum2) and arr_sum2[r]==tmp2:
            r += 1
            c2 += 1
        result += c1*c2
    elif tmp > 0:
        r += 1
    else:
        l += 1

print(result)