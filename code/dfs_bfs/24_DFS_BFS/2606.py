def dfs(start):
    global cnt
    for i in range(1, N+1):
        if visited[i] == 0 and arr[start][i] == 1:
            visited[i] = 1
            cnt += 1
            # print(i)
            dfs(i)


N = int(input())
E = int(input())

arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]


for _ in range(E):
    s, e = map(int, input().split())
    arr[s][e] = 1
    arr[e][s] = 1

cnt = 0
visited[1] = 1
dfs(1)
print(cnt)