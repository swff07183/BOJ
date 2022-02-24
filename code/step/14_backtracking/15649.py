def make_permutation(N, M, cnt):
    if cnt == M:
        print(*result)
        return
    # 1부터 N까지
    for i in range(1, N+1):
        if not visited[i]:  # 아직 방문하지 않았다면
            visited[i] = 1
            result.append(i)
            make_permutation(N, M, cnt + 1)
            visited[i] = 0
            result.pop()


# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
N, M = map(int, input().split())
visited = [0 for _ in range(N+1)]
result = []

make_permutation(N, M, 0)