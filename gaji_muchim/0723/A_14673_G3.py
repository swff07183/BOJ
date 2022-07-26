"""
Crush Fever
"""
import sys
from copy import deepcopy
from collections import deque
sys.stdin = open('input.txt')
input = lambda: sys.stdin.readline().rstrip()

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

def crush(cnt, total, puzzle):
    global ans
    ans = max(ans, total)
    if cnt == 3:
        return
    popped = [[False for _ in range(M)] for _ in range(N)]
    
    for i in range(N):
        for j in range(M):
            if puzzle[i][j] and not popped[i][j]:
                # 눌러서 터트리기!
                # 일단 puzzle 복사한다음에
                tmp = deepcopy(puzzle)
                pop_cnt = 0
                # 인접한 배열 체크해서 0으로 만들어주고
                queue = deque()
                queue.append([i, j])
                v = [[False for _ in range(M)] for _ in range(N)]
                v[i][j] = True
                value = tmp[i][j]
                pop_cnt = 0
                while queue:
                    si, sj = queue.popleft()
                    tmp[si][sj] = 0
                    popped[si][sj] = True
                    pop_cnt += 1
                    for d in range(4):
                        ni = si + di[d]
                        nj = sj + dj[d]
                        if not (0<=ni<N and 0<=nj<M) or v[ni][nj] or tmp[ni][nj] != value:
                            continue
                        queue.append([ni, nj])
                        v[ni][nj] = True

                # 배열 밑으로 내려보내기
                for y in range(M):
                    for x in range(N-2, -1, -1):
                        nx = x
                        while 0 <= nx < N-1 and tmp[nx+1][y] == 0:
                            tmp[nx][y], tmp[nx+1][y] = tmp[nx+1][y], tmp[nx][y]
                            nx += 1

                # 점수 계산하고 dfs 들어가기
                score = pop_cnt * pop_cnt
                crush(cnt+1, total + score, tmp)
            

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
crush(0, 0, arr)
print(ans)