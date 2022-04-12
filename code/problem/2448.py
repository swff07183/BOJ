def tree(n, top_i, top_j):
    if n == 3:
        arr[top_i][top_j] = '*'
        arr[top_i+1][top_j-1:top_j+2] = ['*',' ','*']
        arr[top_i+2][top_j-2:top_j+3] = ['*']*5
    else:
        sz = n//2
        tree(sz, top_i, top_j)
        tree(sz, top_i+sz, top_j-sz)
        tree(sz, top_i+sz, top_j+sz)

N = int(input())
arr = [[" " for _ in range(N*2-1)] for _ in range(N)]
tree(N, 0, N-1)
for row in arr:
    print(''.join(row))