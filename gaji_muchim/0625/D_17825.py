import sys, copy
input = lambda: sys.stdin.readline().rstrip()

mals=[[1, 0], [1, 0], [1, 0], [1, 0]]

def recur(cur, total):
    global ans
    if cur == 10:
        ans = max(ans, total)
        return

    k = arr[cur]    # 몇칸 갈지 계산

    for i in range(4):                                      # 말 4개 탐색
        route, idx = mals[i]
        if not route:                                       # 이미 도착점에 도달했다면
            continue                                        # 안움직이고
        
        n_route, n_idx, n_score = board[route][idx + k]     # 다음 위치 계산
        if n_route == 0:                                    # 도착점이다?
            mals[i] = [n_route, n_idx]                      # 그럼 도착점에 옮겨놓고
            recur(cur+1, total)                             # 다음 탐색
            mals[i] = [route, idx]                          # 되돌아오면 원래대로

        elif [n_route, n_idx] not in mals:                  # 다음 위치에 다른 말이 없다면
            mals[i] = [n_route, n_idx]                      # 보내고
            recur(cur+1, total + n_score)                   # 점수 추가 후 다음 탐색하고
            mals[i] = [route, idx]                          # 되돌아오면 원래대로 놓고
        
    
    
# [경로 번호, 인덱스, 점수]
route1 = [
    [1, 0, 0], [1, 1, 2], [1, 2, 4], [1, 3, 6], [1, 4, 8], [2, 0, 10],
    [1, 6, 12], [1, 7, 14], [1, 8, 16], [1, 9, 18], [3, 0, 20], [1, 11, 22],
    [1, 12, 24], [1, 13, 26], [1, 14, 28], [4, 0, 30], [1, 16, 32], [1, 17, 34],
    [1, 18, 36], [1, 19, 38], [3, 6, 40],
    [0, 0, -1], [0, 0, -1], [0, 0, -1], [0, 0, -1], [0, 0, -1]
    ]
route2 = [
    [2, 0, 10], [2, 1, 13], [2, 2, 16], [2, 3, 19],
    [3, 3, 25], [3, 4, 30], [3, 5, 35], [3, 6, 40],
    [0, 0, -1], [0, 0, -1], 
]
route3 = [
    [3, 0, 20], [3, 1, 22], [3, 2, 24], [3, 3, 25],
    [3, 4, 30], [3, 5, 35], [3, 6, 40],
    [0, 0, -1], [0, 0, -1], [0, 0, -1], [0, 0, -1], [0, 0, -1]
    ]
route4 = [
    [4, 0, 30], [4, 1, 28], [4, 2, 27], [4, 3, 26], 
    [3, 3, 25], [3, 4, 30], [3, 5, 35], [3, 6, 40],
    [0, 0, -1], [0, 0, -1], 
    ]

board = [
    [],
    route1,
    route2,
    route3,
    route4,
]

N = 10
arr = list(map(int, input().split()))
ans = 0
recur(0, 0)
print(ans)