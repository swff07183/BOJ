"""
뉴스 전하기

24
-1 0 0 1 1 1 2 2 3 3 4 4 5 5 6 7 7 8 12 13 14 16 16 16
"""
def get_sz(node):
    ret = 1
    for nxt in graph[node]:
        ret += get_sz(nxt)
    sz[node] = ret
    return sz[node]

def get_time(node):
    graph[node].sort(key=lambda x:-sz[x])
    for i in range(len(graph[node])):
        nxt = graph[node][i]
        time[nxt] = time[node]+i+1
        get_time(nxt)

N = int(input())
arr = list(map(int, input().split()))

graph=[[] for _ in range(N)]
p = [x for x in range(N)]
sz = [1 for _ in range(N)]
time = [0 for _ in range(N)]

for i in range(1, N):
    graph[arr[i]].append(i)
    p[i] = arr[i]

get_sz(0)
get_time(0)
print(max(time))