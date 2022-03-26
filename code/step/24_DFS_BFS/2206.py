import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

from collections import deque

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def bfs(si, sj):
    queue = deque()
    v = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]
    queue.append([(si, sj), 0])
    v[0][si][sj] = 1
    v[1][si][sj] = 1
    result = -1
    while queue:
        data = queue.popleft()
        i, j = data[0]
        block = data[1]
        if i==N-1 and j==M-1:
            # print(v[0][i][j], v[1][i][j])
            result = v[block][i][j]
            break
        for idx_d in range(4):
            ni = i + di[idx_d]
            nj = j + dj[idx_d]
            if (0<=ni<N and 0<=nj<M) and v[block][ni][nj] == 0:
                # 이미 벽을 부수면서 지나왔다면
                if block == 1:
                    if arr[ni][nj] == 0:
                        v[block][ni][nj] = v[block][i][j] + 1
                        queue.append([(ni, nj), 1])
                # 아직 벽을 부수지 않았다면
                else:
                    if arr[ni][nj] == 0:
                        n_block = 0
                        v[0][ni][nj] = v[0][i][j] + 1
                        v[1][ni][nj] = v[0][i][j] + 1
                    else:
                        n_block = 1
                    if v[n_block][ni][nj] == 0:
                        v[n_block][ni][nj] = v[0][i][j] + 1
                    queue.append([(ni, nj), n_block])
    # print("=" * 30)
    # for row in v[0]:
    #     print(*row)
    # print("="*30)
    # for row in v[1]:
    #     print(*row)
    # print("=" * 30)

    return result


N, M = map(int, input().split())

arr = [list(map(int, input().rstrip())) for _ in range(N)]

si, sj = 0, 0

print(bfs(si, sj))