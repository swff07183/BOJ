import sys
input = sys.stdin.readline
from collections import deque

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def ball_sort(balls, d):
    if d == 0:
        return sorted(balls, key=lambda x:x[0])
    elif d == 1:
        return sorted(balls, key=lambda x:x[1])
    elif d == 2:
        return sorted(balls, key=lambda x:-x[0])
    elif d == 3:
        return sorted(balls, key=lambda x:-x[1])

def escape():
    queue = deque()
    queue.append([blue, red])
    v = [[[[False for _ in range(M+1)] for _ in range(N+1)] for _ in range(M+1)] for _ in range(N+1)]
    v[blue[0]][blue[1]][red[0]][red[1]] = True
    cnt = 1
    while queue and cnt <= 10:
        for _ in range(len(queue)):
            balls = queue.popleft()
            for d in range(4):                  # 4방향
                balls = ball_sort(balls, d)     # 공 정렬
                tmp = []
                isHall = {
                    'R': False,
                    'B': False,
                }
                ti, tj = -1, -1
                for i, j, b in balls:           # 공 두개 움직이기
                    while True:
                        ni = i + di[d]
                        nj = j + dj[d]
                        if arr[ni][nj] == '#' or (ni==ti and nj==tj):
                            ti, tj = i, j
                            tmp.append([i, j, b])
                            break
                        elif arr[ni][nj] == "O":
                            isHall[b] = True
                            break
                        else:
                            i, j = ni, nj
                if isHall['R'] and not isHall['B']:
                    return cnt
                elif not isHall['B']:
                    tmp.sort(key=lambda x:x[2])
                    if not (v[tmp[0][0]][tmp[0][1]][tmp[1][0]][tmp[1][1]]):
                        v[tmp[0][0]][tmp[0][1]][tmp[1][0]][tmp[1][1]] = True
                        queue.append(tmp)
        cnt += 1
    return -1
            


N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]

for i in range(1, N-1):
    for j in range(1, M-1):
        if arr[i][j] == 'B':
            blue = [i, j, 'B']
        elif arr[i][j] == 'R':
            red = [i, j, 'R']

result = escape()
print(result)