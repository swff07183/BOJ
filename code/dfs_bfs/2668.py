def dfs(node, group):
    global last_node
    nxt = arr[node]
    if not v[nxt]:
        v[node] = group
        tmp = dfs(nxt, group)
        v[node] = tmp
        if node == last_node:
            last_node = -1
            return -1
        return v[node]
    elif v[nxt] != group:
        v[node] = -1
        return -1
    elif v[nxt] == group:
        v[node] = group
        last_node = nxt
        return group

N = int(input())

arr = [0] + [int(input()) for _ in range(N)]

cnt = 1  # 그룹 만들기
v = [0 for _ in range(N+1)]
last_node = -1

for i in range(1, N+1):
    if not v[i]:
        # v[i] = cnt
        dfs(i, cnt)
        cnt += 1

result = []
for i in range(1, N+1):
    if v[i] != -1:
        result.append(i)

print(len(result))
for x in result:
    print(x)