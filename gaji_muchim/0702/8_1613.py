"""
역사

단방향 그래프에서
해당 점에서 특정 점으로 갈수 있는지 없는지 체크해서
a->b로 갈 수 있다 ? a가 먼저 일어난 것
b->a로 갈 수 있다 ? b가 먼저 일어난 것

그래서 2차원 배열 check 만들고
i (1~n)에서 시작해서 dfs ㄱㄱ
i->j 로 갈수있으면 : check[i][j]=True로 바꿔주기
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(start, node):
    check[start][node] = True
    for nxt in graph[node]:
        if check[start][nxt]:
            continue
        dfs(start, nxt)

n, k = map(int, input().split())

check = [[False for _ in range(n+1)] for _ in range(n+1)]
graph = [[] for _ in range(n+1)]

for _ in range(k):
    x, y = map(int, input().split())
    graph[x].append(y)

for i in range(1, n+1):
    dfs(i, i)

s = int(input())
for _ in range(s):
    x, y = map(int, input().split())
    if check[x][y]:
        print(-1)
    elif check[y][x]:
        print(1)
    else:
        print(0)