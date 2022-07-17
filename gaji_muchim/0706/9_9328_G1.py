"""
key 얻었을 시에, 그 해당하는 문에 순간이동 하도록 만들어보자자자자자
"""
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def is_upper(c):
    # 대문자인지 확인하는 함수
    return 'A' <= c <= 'Z'

def is_lower(c):
    # 소문자인지 확인하는 함수
    return 'a' <= c <= 'z'

def in_range(i, j):
    # 범위 안에 있는지 확인하는 함수
    return 0 <= i < h and 0 <= j < w

def bfs():
    global ans
    queue = deque()
    for i, j in start:
        queue.append([i, j])
    while queue:
        i, j = queue.popleft()
        for d in range(4):
            ni = i + di[d]
            nj = j + dj[d]
            if not in_range(ni, nj) or visited[ni][nj] or arr[ni][nj] == '*':
                continue

            if arr[ni][nj]=='.':
                pass

            elif is_upper(arr[ni][nj]):
                found[ni][nj] = True
                k = arr[ni][nj]
                if not keys.get(k):
                    continue

            elif is_lower(arr[ni][nj]):
                k = arr[ni][nj].upper()
                if not keys.get(k):
                    keys[k] = True
                    for x, y in doors.get(k, []):
                        if found[x][y] and not visited[x][y]:
                            visited[x][y] = True
                            queue.append([x, y])
                            
            elif arr[ni][nj] == '$':
                ans += 1
                arr[ni][nj] == '.'
                
            visited[ni][nj] = True
            queue.append([ni, nj])


di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]

T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    
    keys = {c:True for c in input().upper()}
    found = [[False for _ in range(w)] for _ in range(h)]
    visited = [[False for _ in range(w)] for _ in range(h)]
    doors = {}
    start = []
    ans = 0

    for i in range(h):
        for j in [0, w-1]:
            if arr[i][j] != '*':
                if arr[i][j] == '.':
                    pass
                elif arr[i][j] == '$':
                    ans += 1
                    arr[i][j] = '.'
                elif is_upper(arr[i][j]):
                    found[i][j] = True
                    if not keys.get(arr[i][j]):
                        continue
                elif is_lower(arr[i][j]):
                    k = arr[i][j].upper()
                    keys[k] = True
                visited[i][j] = True
                start.append([i, j])
    for j in range(1, w-1):
        for i in [0, h-1]:
            if arr[i][j] != '*':
                if arr[i][j] == '.':
                    pass
                elif arr[i][j] == '$':
                    ans += 1
                    arr[i][j] = '.'
                elif is_upper(arr[i][j]):
                    found[i][j] = True
                    if not keys.get(arr[i][j]):
                        continue
                elif is_lower(arr[i][j]):
                    k = arr[i][j].upper()
                    keys[k] = True
                visited[i][j] = True
                start.append([i, j])
    for i in range(h):
        for j in range(w):
            if is_upper(arr[i][j]):
                doors[arr[i][j]] = doors.get(arr[i][j], []) + [(i, j)]

    bfs()
    print(ans)