n = int(input())
# a[i] - a[i+1] = a[i+2]
res = 0
idx = 0
for i in range(1, n + 1):
    arr = [0] * (n + 5)  # arr 넉넉하게
    arr[0] = n
    arr[1] = i  # 두번째 수는 i로 고르기
    cnt = 1
    for j in range(2, n+5): # 요것도 넉넉하게 돌리기 -> 음수 되면 break되니까!
        arr[j] = arr[j - 2] - arr[j - 1]
        cnt += 1
        # print(arr)

        if cnt > res:
            res = cnt
            idx = i

        if arr[j] < 0:
            break

print(res)
li = [n]
li.append(idx)  # 두번째 수는 idx

for i in range(2, res):
    li.append(li[i - 2] - li[i - 1])

print(*li)