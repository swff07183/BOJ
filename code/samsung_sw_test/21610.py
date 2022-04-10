import sys
input = sys.stdin.readline

# d : 1~8, W 부터 시계방향
di = [0,  0, -1, -1, -1, 0, 1, 1,  1]
dj = [0, -1, -1,  0,  1, 1, 1, 0, -1]

# c : 0~3, 대각선 방향
ci = [-1, -1, 1, 1]
cj = [-1, 1, -1, 1]

def get_cloud():
    result = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and (i, j) not in clouds:
                arr[i][j] -= 2
                result.append((i, j))
    return result

def rain(clouds):
    for i, j in clouds:
        arr[i][j] += 1

def water_bug(clouds):
    for i, j in clouds:
        cnt = 0
        for c in range(4):
            ni = i + ci[c]
            nj = j + cj[c]

            if not(0<=ni<N and 0<=nj<N) or arr[ni][nj] == 0:
                continue
            cnt += 1
        arr[i][j] += cnt


def move_cloud(clouds, d, s):
    result = []
    for i, j in clouds:
        ni = (i + di[d]*s) % N
        nj = (j + dj[d]*s) % N
        result.append((ni, nj))
    return result

def print_arr():
    for row in arr:
        print(*row)
    print('='*70)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for num in range(1, M+1):
    d, s = map(int, input().split())
    # 1. 모든 구름이 d 방향으로 s칸 이동한다.
    clouds = move_cloud(clouds, d, s)
    # 2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
    rain(clouds)
    # 3. 구름이 모두 사라진다.
    # 4. 2에서 물이 증가한 (r,c)에 물 복사버그 마법을 시전한다.
    water_bug(clouds)
    # 5. 바구니에 저장된 물의 양이 2이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
    clouds = get_cloud()


print(sum(sum(arr, [])))