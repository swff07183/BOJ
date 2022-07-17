# 삽질의 흔적

# def recur(nodes, som=0, yeon=0):
#     global func_call, result
#     if len(nodes) > 7 or yeon > 4:
#         return
#     func_call += 1
#     cand = []
#     if len(nodes) == 7:
#         print(func_call, *nodes)
#         print('='*50)
#         result += 1
#     for i, j in nodes:
#         for d in range(2):
#             ni = i + di[d]
#             nj = j + dj[d]
#             if not (0 <= ni < N and 0 <= nj < N) or v[ni][nj]:
#                 continue
#             v[ni][nj] = True
#             recur(nodes + [[ni, nj]])
#             cand.append([ni, nj])
#             v[ni][nj] = False
#     if len(cand) == 2:
#         for i, j in cand:
#             v[i][j] = True
#         recur(nodes + cand)
#         for i, j in cand:
#             v[i][j] = False
    
import sys
input = lambda: sys.stdin.readline().rstrip()

di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

def dfs(cur, i, j, nodes, v):
    # 요소가 전부 연결되었는지 확인하기
    cnt = 1 
    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if (0<=ni<N and 0<=nj<N) and not v[ni][nj] and ([ni, nj] in nodes):
            v[ni][nj] = True
            cnt += dfs(cur+1, ni, nj, nodes, v)
    return cnt


def check(nodes):
    i, j = nodes[0]
    v = [[False for _ in range(N)] for _ in range(N)]
    v[i][j] = True
    ret = dfs(0, i, j, nodes, v)

    return ret
    

def recur(cur, start, tmp):
    global result, yeon
    if yeon >= 4:   # 연이 4 이상 -> 어차피 다솜파가 4명이상 안되니까 가지치기
        return
    if cur == 7:    # 7명 다 뽑았을 때 연결되어있는지 확인하기
        if check(tmp) >= 7:        
            result += 1
        return
    
    for i in range(N):
        for j in range(N):
            idx = i*5 + j   # 5*5 -> 0~24까지 번호 매기기
            if idx > start:
                yeon += (1 - arr[i][j])
                recur(cur+1, idx, tmp + [[i, j]])
                yeon -= (1 - arr[i][j])
                

    

N = 5
arr = [list(map(lambda x:int(x=='S'), input())) for _ in range(N)]
nodes = [[i, j] for i in range(N) for j in range(N)]

result = 0
yeon = 0

recur(0, -1, [])
print(result)