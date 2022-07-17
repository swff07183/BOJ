import sys, copy
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def block(board):
    """
    블럭이 있는 위치 찾기
    """
    blocks = []
    for i in range(N):
        for j in range(N):
            if board[i][j]:
                blocks.append([i, j, board[i][j]])
    return blocks

def sort_block(blocks, d):
    """
    상: i 오름차순
    하: i 내림차순
    좌: j 오름차순
    우: j 내림차순
    """
    if d==0:
        blocks = sorted(blocks, key=lambda x: x[0])
    elif d==1:
        blocks = sorted(blocks, key=lambda x: -x[0])
    elif d==2:
        blocks = sorted(blocks, key=lambda x: x[1])
    elif d==3:
        blocks = sorted(blocks, key=lambda x: -x[1])
    return blocks

def in_range(i, j):
    return (0 <= i < N and 0 <= j < N)

def simul():
    global result
    queue = deque()
    queue.append(copy.deepcopy(arr))

    # 최대 5번 이동시킬꺼다
    for cnt in range(5):
        tmp = deque()
        while queue:
            board_s = queue.popleft()
            # 출력
            # for row in board_s:
            #     print(*row)
            # print('=' * 50)

            blocks = block(board_s)                # 숫자판 있는 위치 찾고

            for d in range(4):                      # 4방향에 대해서 움직이기
                board = [[0 for _ in range(N)] for _ in range(N)]
                blocks = sort_block(blocks[:], d)   # 방향에 맞게 위치들 정렬
                check = []                          # 이미 합쳐진 위치 체크할 리스트
                
                for i, j, v in blocks:
                    while True:
                        ni = i + di[d]              # 다음 위치 계산 계속 할꺼다
                        nj = j + dj[d]

                        if not in_range(ni, nj):    # 범위 밖으로 벗어났다면
                            board[i][j] = v         # 그 위치에 블록 추가하기
                            break

                        if board[ni][nj]:           # 만약 이미 블록이 있다?
                                                    # 값이 같고 이번에 합쳐지지 않았다면
                            if board[ni][nj] == v and [ni, nj] not in check:
                                board[ni][nj] += v  # 합치기
                                check.append([ni, nj])
                            else:
                                board[i][j] = v     # 아니면 그 직전에 블록 멈추기
                            break

                        i, j = ni, nj

                result = max(result, max(map(max, board)))
                tmp.append(copy.deepcopy(board))
        queue = tmp
                    
            


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
simul()
print(result)
"""
N^2 * 4방향 ** 5번
"""