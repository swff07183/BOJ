T = int(input())

for tc in range(1, T+1):
    n = int(input())
    cnt = [[1, 0], [0, 1], [1, 1]]
    for i in range(3, n+1):
        cnt_0 = cnt[i-1][0] + cnt[i-2][0]
        cnt_1 = cnt[i-1][1] + cnt[i-2][1]
        cnt.append([cnt_0, cnt_1])
    print(*cnt[n])