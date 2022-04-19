import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def dfs(node, cnt):
    global result
    if v[node] == True:
        return node, cnt
    v[node] = True
    nxt = arr[node]

    ret, c = dfs(nxt, cnt+1)
    if ret == node:
        result -= (c-cnt)

    return ret, c

    
T = int(input())
for tc in range(1, T+1):

    N = int(input())
    arr = [0] + list(map(int, input().split()))
    v = [False for _ in range(N+1)]
    
    result = N

    for i in range(1, N+1):
        if not v[i]:
            dfs(i, 0)
            
    print(result)