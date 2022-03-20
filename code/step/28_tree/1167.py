# 트리 지름 구하기  https://blog.myungwoo.kr/112

def dfs(start, total):
    global max_distance, u
    if total > max_distance:
        max_distance = total
        u = start
    for node, distance in tree[start]:
        if visited[node] == 0:
            visited[node] = 1
            dfs(node, total + distance)
            visited[node] = 0
    return

V = int(input())

tree = [[] for _ in range(V+1)]
max_distance = 0
u = -1

for _ in range(V):
    data = list(map(int, input().split()))
    node_s = data[0]
    i = 1
    while True:
        node_e = data[i]
        if node_e == -1:
            break
        distance = data[i+1]
        tree[node_s].append((node_e, distance))
        i += 2

visited = [0 for _ in range(V+1)]
visited[1] = 1
dfs(1, 0)

visited = [0 for _ in range(V+1)]
visited[u] = 1
dfs(u, 0)

print(max_distance)