import sys
sys.setrecursionlimit(10000)
sys.stdin = open('input.txt')
input = sys.stdin.readline

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def dfs(i, j):
    ret = 0
    if i==M-1 and j==N-1:       # 도착점에 도달했다면
        dp[i][j] = 1        
        return dp[i][j]         # 1 리턴
    if dp[i][j] != -1:          # 이미 해당 지점이 도착점으로 갈 수 있다면?
        return dp[i][j]         # 도착지점으로 가는 가지수 리턴

    dp[i][j] = 0                # 경우의 수 계산하기 위해 0 저장
    for d in range(4):          # 상, 하, 좌, 우 탐색
        ni = i + di[d]
        nj = j + dj[d]
        if not (0<=ni<M and 0<=nj<N) or arr[ni][nj] >= arr[i][j]:
            continue            # 해당 좌표 갈 수 없다면 다음 좌표 탐색
        dp[i][j] += dfs(ni, nj) # 해당 좌표에서 정답으로 가는 경우 찾기
    return dp[i][j]


M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)] # 방문한지 안한지 확인하기 위해 -1로 초기화

dfs(0, 0)
print(dp[0][0])