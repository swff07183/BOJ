import sys
input = sys.stdin.readline

def box_num(i, j):
    return (i//3)*3 + (j//3)

def recur(cur):
    if cur == zero_cnt:
        for row in arr:
            print(*row)        
        exit()
    i, j = data[cur]
    for num in range(1, 10):
        if check_row[i][num] or check_col[j][num] or check_box[box_num(i, j)][num]:
            continue
        check_row[i][num] = True
        check_col[j][num] = True
        check_box[box_num(i, j)][num] = True
        arr[i][j] = num

        recur(cur+1)

        arr[i][j] = 0
        check_row[i][num] = False
        check_col[j][num] = False
        check_box[box_num(i, j)][num] = False

N = 9
arr = [list(map(int, input().split())) for _ in range(N)]
data = []
zero_cnt = 0
check_row = [[False for _ in range(N+1)] for _ in range(N+1)]
check_col = [[False for _ in range(N+1)] for _ in range(N+1)]
check_box = [[False for _ in range(N+1)] for _ in range(N+1)]


for i in range(N):
    for j in range(N):
        if not arr[i][j]:
            data.append((i, j))
            zero_cnt += 1
        else:
            check_row[i][arr[i][j]] = True
            check_col[j][arr[i][j]] = True
            check_box[box_num(i, j)][arr[i][j]] = True

recur(0)

for row in arr:
    print(*row)