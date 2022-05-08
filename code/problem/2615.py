import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

def check_omok(i, j):
    player = arr[i][j]
    # 세로 방향 확인
    cnt = 1
    for di in range(1, 5):
        ni = i + di
        if not (0 <= ni < N):
            continue
        cnt += 1 if arr[ni][j]==player else 0
    if cnt == 5:
        for di in (-1, 5):
            ni = i + di
            if not (0 <= ni < N):
                continue
            cnt += 1 if arr[ni][j]==player else 0
        if cnt == 5:
            return (i+1, j+1)
    # 가로 방향 확인
    cnt = 1
    for dj in range(1, 5):
        nj = j + dj
        if not (0 <= nj < N):
            continue
        cnt += 1 if arr[i][nj]==player else 0
    if cnt == 5:
        for dj in (-1, 5):
            nj = j + dj
            if not (0 <= nj < N):
                continue
            cnt += 1 if arr[i][nj]==player else 0
        if cnt == 5:
            return (i+1, j+1)
    # 오른쪽 위 방향 확인
    cnt = 1
    for dk in range(1, 5):
        ni = i - dk
        nj = j + dk
        if not (0 <= ni < N and 0 <= nj < N):
            continue
        cnt += 1 if arr[ni][nj]==player else 0
    if cnt == 5:
        for dk in (-1, 5):
            ni = i - dk
            nj = j + dk
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            cnt += 1 if arr[ni][nj]==player else 0
        if cnt == 5:
            return (i+1, j+1)
    # 오른쪽 아래 방향 확인
    cnt = 1
    for dk in range(1, 5):
        ni = i + dk
        nj = j + dk
        if not (0 <= ni < N and 0 <= nj < N):
            continue
        cnt += 1 if arr[ni][nj]==player else 0
    if cnt == 5:
        for dk in (-1, 5):
            ni = i + dk
            nj = j + dk
            if not (0 <= ni < N and 0 <= nj < N):
                continue
            cnt += 1 if arr[ni][nj]==player else 0
        if cnt == 5:
            return (i+1, j+1)
    
    return False

N = 19
arr = [list(map(int, input().split())) for _ in range(N)]

for j in range(N):
    for i in range(N):
        if arr[i][j]:
            tmp = check_omok(i, j)
            if tmp:
                print(arr[i][j])
                print(*tmp)
                exit(0)

print(0)