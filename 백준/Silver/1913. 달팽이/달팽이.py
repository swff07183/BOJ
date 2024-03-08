di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def recur():
    global ans

    i, j = N//2, N//2
    d = 0
    cnt = 1
    for x in range(1, N+1):
        for _ in range(2):
            for _ in range(x):
                arr[i][j] = cnt
                if cnt == M:
                    ans = [i+1, j+1]
                cnt += 1
                if cnt > N*N:
                    return
                i += di[d]
                j += dj[d]
            d = (d + 1) % 4

N = int(input())
M = int(input())

arr = [[0 for _ in range(N)] for _ in range(N)]

ans = [-1, -1]

recur()
    
        
for row in arr:
    print(*row)

print(*ans)