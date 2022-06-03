def solution(m, n, board):
    answer = 0
    di = [1, 0, 1, 0]
    dj = [0, 1, 1, 0]
    
    board = [list(row) for row in board]
    
    def isBlock(i, j):
        tmp = board[i][j]
        if not tmp:
            return False
        for d in range(3):
            ni = i + di[d]
            nj = j + dj[d]
            if board[ni][nj] != tmp:
                return False
        return True

    def checkBlock(i, j):
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            check[ni][nj] = True

    def eraseBlock():
        cnt = 0
        for i in range(m):
            for j in range(n):
                if check[i][j]:
                    board[i][j] = ''
                    cnt += 1
        return cnt

    def moveBlock(i, j):
        while i < m-1 and not board[i+1][j]:
            board[i+1][j], board[i][j] = board[i][j], board[i+1][j]
            i += 1
    
    while True:
        check = [[False for _ in range(n)] for _ in range(m)]
        for j in range(n-1):
            for i in range(m-1):
                if isBlock(i, j):
                    checkBlock(i, j)
        
        cnt = eraseBlock()
        if cnt == 0:
            break
        answer += cnt
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                moveBlock(i, j)
    
    return answer