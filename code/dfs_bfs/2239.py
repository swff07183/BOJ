import sys
input = sys.stdin.readline

def check_(i, j):
    tmp = arr[i][j]
    return not (row[i][tmp] or col[j][tmp] or box[i//3][j//3][tmp])
        


def sudoku(si, sj, cnt):
    if cnt == cnt_0:
        for r in arr:
            print(*r, sep='')
        exit(0)
    i, j = pos_0[cnt]
    for n in range(1, 10):
        arr[i][j] = n
        if row[i][n] or col[j][n] or box[i//3][j//3][n]:
            continue
        row[i][n] = True
        col[j][n] = True
        box[i//3][j//3][n] = True
        sudoku(i, j, cnt+1)
        row[i][n] = False
        col[j][n] = False
        box[i//3][j//3][n] = False
    arr[i][j] = 0


arr = [list(map(int, input().rstrip())) for _ in range(9)]
pos_0 = []
cnt_0 = 0

row = [[False for _ in range(10)] for _ in range(9)]
col = [[False for _ in range(10)] for _ in range(9)]
box = [[[False for _ in range(10)] for _ in range(3)] for _ in range(3)]


for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            pos_0.append((i, j))
            cnt_0 += 1
        else:
            tmp = arr[i][j]
            row[i][tmp] = True
            col[j][tmp] = True
            box[i//3][j//3][tmp] = True
            

sudoku(0, 0, 0)


