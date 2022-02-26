di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

def alpha(cnt, x, y):
    global max_cnt
    for i in range(4):
        ni = x + di[i]
        nj = y + dj[i]
        if 0 <= ni < R and 0 <= nj < C:
            idx_a = ord(data[ni][nj]) - ord('A')
            if visited[ni][nj] == 0 and check[idx_a] == 0:
                visited[ni][nj] = 1
                check[idx_a] = 1
                if max_cnt < cnt+1:
                    max_cnt = cnt+1
                alpha(cnt+1, ni, nj)
                visited[ni][nj] = 0
                check[idx_a] = 0
                # print(cnt)


max_cnt = 1

# R : 세로
# C : 가로
R, C = map(int, input().split())
data = [list(input()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
check = [0 for _ in range(26)]
visited[0][0] = 1
i = ord(data[0][0]) - ord('A')
check[i] = 1

alpha(1, 0, 0)
print(max_cnt)