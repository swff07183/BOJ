import sys
sys.stdin = open('input.txt')
from collections import deque
# input = sys.stdin.readline

def bfs():
    v = [-1 for _ in range(101)]
    v[1] = 0
    queue = deque()
    queue.append(1)
    
    while queue:
        pos = queue.popleft()
        # print(pos, v[pos])
        if pos == 100:
            print(v[pos])
            return
        for i in range(1, 7):
            npos = pos + i
            # print(npos)
            if 0<=npos<=100 and v[npos] == -1:
                if arr[npos] != -1:
                    if v[arr[npos]] == -1:
                        v[arr[npos]] = v[pos] + 1
                        npos = arr[npos]
                        queue.append(npos)
                else:
                    v[npos] = v[pos] + 1
                    queue.append(npos)
    

N, M = map(int, input().split())
arr = [-1 for _ in range(101)]
for _ in range(N+M):
    x, y = map(int, input().split())
    arr[x] = y

bfs()