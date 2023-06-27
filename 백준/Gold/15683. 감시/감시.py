import sys
input = lambda : sys.stdin.readline().rstrip()

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

def recur(cur):
    global result, blank_cnt
    if cur == cctv_cnt:
        result = min(result, blank_cnt)
        return
    i, j = cctv[cur]
    for k in range(4):
        check = []
        for d in monitor[arr[i][j]]:
            ni, nj = i, j
            d = (d + k) % 4
            while True:
                ni += di[d]
                nj += dj[d]
                if not (0<=ni<N and 0<=nj<M) or arr[ni][nj] == 6:
                    break
                if arr[ni][nj] == 0:
                    arr[ni][nj] = f'#{cur}'
                    blank_cnt -= 1
                    check.append([ni, nj])
        
        recur(cur+1)

        for ni, nj in check:
            arr[ni][nj] = 0
            blank_cnt += 1

            


monitor = {
    1: [1],
    2: [1, 3],
    3: [0, 1],
    4: [0, 1, 3],
    5: [0, 1, 2, 3],
}

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

cctv = []
cctv_cnt = 0
blank_cnt = N*M
result = N*M+1

for i in range(N):
    for j in range(M):
        if 1 <= arr[i][j] <= 5:
            cctv.append([i, j])
            cctv_cnt += 1
        if arr[i][j]:
            blank_cnt -= 1


recur(0)
print(result)