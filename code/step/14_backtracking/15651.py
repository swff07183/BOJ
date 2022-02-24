def make_permutation(N, M, cnt, last_num=1):
    if cnt == M:
        print(*result)
        return
    # 1부터 N까지
    for i in range(last_num, N+1):
        result.append(i)
        make_permutation(N, M, cnt + 1, i)
        result.pop()


N, M = map(int, input().split())
result = []

make_permutation(N, M, 0)