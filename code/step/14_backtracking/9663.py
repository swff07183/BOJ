di = [-1, -1]
dj = [-1, 1]


def check(x, y):
    # 현재 위치에서 왼쪽 위, 오른쪽 위에 퀸이 있는지 확인
    for j in range(2):
        nx, ny = x, y
        while True:
            nx += di[j]
            ny += dj[j]
            if nx < 0 or ny >= N or ny < 0:
                break
            if arr[nx][ny]:
                return False
    return True


def n_queen(cnt):
    global global_cnt
    if cnt == N:
        # 퀸이 N개 놓여져있다면 횟수 1 증가시키고 리턴
        global_cnt += 1
        return
    for i in range(N):
        if visited[i] == 0 and check(cnt, i):   # 같은 열에 놓여있지 않고, 왼쪽위, 오른쪽 위에 퀸이 없으면
            arr[cnt][i] = 1     # 퀸 놓기
            visited[i] = 1      # 해당 열 체크
            n_queen(cnt + 1)    # 다음 행에 놓기
            arr[cnt][i] = 0     # 끝났으면 원래대로 돌리기
            visited[i] = 0
    return


N = int(input())
arr = [[0 for _ in range(N)] for _ in range(N)] # 체스 판
visited = [0 for _ in range(N)]                 # 열에 퀸이 놓여있는지 체크할 리스트
global_cnt = 0                                  # 리스트

result = n_queen(0)
print(global_cnt)
