import sys
input = sys.stdin.readline

def d(p1, p2):
    return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

def get_chicken_d(subset):
    distance = 0
    chickens = []
    for i in range(num_chicken):
        if subset[i] == 1:
            chickens.append(chicken[i])
    for h in house:
        distance += min([d(h, c) for c in chickens])

    return distance
    
    
def d_chicken(num, cnt, subset):
    global result
    if num == num_chicken:
        if cnt == M:
            result = min(result, get_chicken_d(subset))
        return
    d_chicken(num+1, cnt+1, subset + [1])
    d_chicken(num+1, cnt, subset + [0])
     
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

result = 999999

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            house.append((i, j))
        if arr[i][j] == 2:
            chicken.append((i, j))

num_chicken = len(chicken)

d_chicken(0, 0, [])
print(result)