import sys
input = lambda: sys.stdin.readline().rstrip()

di = [0, -1, 1, 0, 0]
dj = [0, 0, 0, 1, -1]


def simul():
    global result

    for pos in range(1, C+1):
        # 상어 찾기
        shark_pos = -1
        for c in range(1, R+1):
            if arr[c][pos] != 0:
                shark_pos = c
                break
        # 상어 잡기
        if shark_pos != -1:
            result += arr[c][pos][2]
            arr[c][pos] = 0

        # 상어 위치 찾기
        shark_pos = []
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                if arr[i][j]:
                    shark_pos.append([i, j, arr[i][j]])
                    arr[i][j] = 0
        
        # 상어 이동
        for i, j, shark in shark_pos:
            s, d, z = shark
            for _ in range(s):
                ni = i + di[d]
                nj = j + dj[d]
                if not in_range(ni, nj):
                    d = change_pos(d)
                    ni = i + di[d]
                    nj = j + dj[d]
                i, j = ni, nj
            if arr[i][j]:
                if arr[i][j][2] < z:
                    arr[i][j] = [s, d, z]
            else:
                arr[i][j] = [s, d, z]                  

def change_pos(d):
    pos_dict = {
        1: 2,
        2: 1,
        3: 4,
        4: 3,
    }
    return pos_dict[d]

def in_range(i, j):
    return 1<=i<=R and 1<=j<=C

R, C, M = map(int, input().split())
arr = [[0 for _ in range(C+1)] for _ in range(R+1)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    arr[r][c] = [s, d, z]

result = 0
simul()
print(result)