"""
14502

3 ≤ N, M ≤ 8

1: 벽, 2: 바이러스

벽을 3개 세울 수 있음
새로 세우는 벽 *

2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

빈칸 8*8 = 64
벽을 3개 세울

64C3

1. 벽 세울 좌표 3개 고름.
2. 벽 세워
3. 바이러스 퍼트려
4. 안전영역 체크해서 최대값 비교.
"""

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

# 1. 벽 세울 좌표 3개 골라야함.
def combi(lastChoice=-1, tmp=[]):
    if len(tmp) == 3:
        check(tmp)
        return
    
    for i in range(lastChoice+1, len(space)):
        combi(i, tmp + [space[i]])

def in_range(i, j):
    return 0 <= i < N and 0 <= j < M

def dfs(i, j, arr):
    """
    i, j 현재 위치
    ni, nj 다음위치
    4방향 계산할꺼야
    """

    for d in range(4):
        ni = i + di[d]
        nj = j + dj[d]
        if not in_range(ni, nj) or visited[ni][nj] or arr[ni][nj] == 1:
            continue

        # ni, nj 탐색
        visited[ni][nj] = True
        arr[ni][nj] = 2
        dfs(ni, nj, arr)
            


# 2 => 3 => 4
def check(walls):
    """
    walls: [[0, 0], [0, 1], [0, 2]]
    """
    global ans
    # arr 배열 복사
    arr = []
    for row in lab:
        arr.append(row[::])

    # 2. 벽 세운다.
    for i, j in walls:
        arr[i][j] = 1
    
    # 3. 바이러스 퍼트려
    # dfs 로 구현
    for i in range(N):
        for j in range(M):
            # 만약에 바이러스면 시작점 부터 dfs 할꺼임
            if arr[i][j] == 2 and not visited[i][j]:
                visited[i][j] = True
                dfs(i, j, arr)
    
        
    # 4. 안전영역 체크해서 최대값 비교
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                cnt += 1
    
    ans = max(ans, cnt)

    # visited 다시 False 로 바꿔주기
    for i in range(N):
        for j in range(M):
            visited[i][j] = False
    


N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]

ans = 0

# 1차원 배열로 빈 공간 좌표 만들어줄꺼임
space = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 0:
            space.append([i, j])

# 1. 벽 세울 좌표 3개 고름.
combi()

print(ans)