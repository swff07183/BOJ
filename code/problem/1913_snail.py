import sys
sys.stdin = open("input.txt")

N = int(input())
target = int(input())

def snail(n, target):
    arr = [[0 for _ in range(N)] for _ in range(N)]
    di = [-1, 0, 1, 0]
    dj = [0, 1, 0, -1]

    i = n // 2
    j = n // 2
    idx_d = 0

    num = 1
    arr[i][j] = num
    for cnt in range(1, N+1):
        for _ in range(2):
            for _ in range(cnt):
                i += di[idx_d]
                j += dj[idx_d]
                num += 1
                if num > N**2:
                    return arr, pos
                arr[i][j] = num
                if num == target:
                    pos = [i+1, j+1]
            idx_d += 1
            if idx_d == 4:
                idx_d = 0

result, pos = snail(N, target)
for row in result:
    for num in row:
        print(num, end=" ")
    print()

print(pos[0], pos[1])