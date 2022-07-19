"""
나무 재테크
N : 배열의 크기
M : 나무 정보의 개수
K : K년 후 살아남은 나무의 수
arr : 겨울에 각 칸에 추가되는 양분의 크기

처음에는 모든 칸에 양분이 있다.
"""
import sys
sys.stdin = open('input.txt')
input = lambda: sys.stdin.readline().rstrip()


di = [-1, -1, -1, 0, 0,  1, 1, 1]
dj = [-1, 0,  1, -1, 1, -1, 0, 1]
def spring():
    """
    봄에는 나무가 자신의 나이만큼 양분을 먹고, 나이가 1 증가
    양분은 나무가 있는 칸 안에서만 먹을 수 있음
    어린 나무부터 양분 먹는다.
    양분을 못먹으면 즉시 사망
    """
    for i in range(N):
        for j in range(N):
            trees[i][j].sort(reverse=True)      # pop 할꺼라 reverse=True로 해줬음
            tmp = []                            # 살아있는 나무 저장할 리스트
            while trees[i][j]:
                tree = trees[i][j].pop()        # 나이 어린 순서대로 꺼내서
                if tree <= foods[i][j]:         # 양분 먹을 수이쓰면
                    foods[i][j] -= trees        # 양분 개수 줄이고
                    tmp.append(tree+1)          # 살아있는 나무에 추가하고
                else:
                    dead[i][j].append(tree)     # 죽었으면 죽은거에 추가함
            trees[i][j] = tmp[:]                # 다 돌린 다음 살아있는 나무에 추가하고

def summer():
    """
    여름에는 봄에 죽은 나무가 양분으로 변하게 된다.
    양분의 양: 나이 // 2
    """
    for i in range(N):
        for j in range(N):
            while dead[i][j]:
                foods[i][j] += (dead[i][j].pop() // 2)  # 죽은 나무들 체크해서 양분으로 변함
def fall():
    """
    나이가 5의 배수인 나무가 번식함
    인접한 8개의 칸에 나이가 1인 나무가 생성.
    """
    for i in range(N):
        for j in range(N):
            for tree in trees[i][j]:                    # 그다음 트리 있는 녀석들 체크해서
                if tree % 5 == 0:                       # 이거 5의 배수다?
                    for d in range(8):                  # 그럼 8방향
                        ni = i + di[d]
                        nj = j + dj[d]
                        if not (0<=ni<N and 0<=nj<N):
                            continue
                        trees[ni][nj].append(1)         # 나이 1짜리인 나무 추가

def winter():
    """
    S2D2 가 양분을 arr[i][j] 만큼 추가함
    """
    for i in range(N):
        for j in range(N):
            foods[i][j] += arr[i][j]                    # 양분 추가함

def years():
    spring()                                            # 봄
    summer()                                            # 여름
    fall()                                              # 가을
    winter()                                            # 겨울~

N, M, K = map(int, input().split())
trees = [[[] for _ in range(N)] for _ in range(N)]
dead = [[[] for _ in range(N)] for _ in range(N)]
foods = [[5 for _ in range(N)] for _ in range(N)]
arr = [list(map(int, input().split())) for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x-1][y-1].append(z)

ans = 0
for _ in range(K):
    years()

for i in range(N):
    for j in range(N):
        ans += len(trees[i][j])

print(ans)