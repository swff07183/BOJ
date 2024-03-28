from collections import deque

di = [-1, 0, 1, 0, -1, -1, 1, 1]
dj = [0, -1, 0, 1, -1, 1, -1, 1]

def bfs(si, sj):
    # 1. 시작점 queue에 넣고 방문 체크 한다.
    queue = deque()
    queue.append([si, sj])
    visited[si][sj] = True

    # 2. queue에 남아있을 때 까지 반복한다.
    while queue:
        i, j = queue.popleft()
        for d in range(8):
            ni = i + di[d]
            nj = j + dj[d]
            if not (0<=ni<h and 0<=nj<w) or visited[ni][nj] or island[ni][nj] == 0:
                continue

            visited[ni][nj] = True
            queue.append([ni, nj])
    


while True:
    w, h = map(int, input().split())
    if (w == 0 and h == 0):
        break
    island = [list(map(int, input().split())) for _ in range(h)]
    
    visited = [[False for _ in range(w)] for _ in range(h)]
    ans = 0
    for i in range(h):
        for j in range(w):
            if (island[i][j] == 1 and visited[i][j] == False):
                bfs(i, j)
                ans += 1
    
    print(ans)


