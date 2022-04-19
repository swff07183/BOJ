import sys, heapq
sys.stdin = open('input.txt')
input = sys.stdin.readline

def find_(x):
    if x == p[x]:
        return x
    else:
        p[x] = find_(p[x])
        return p[x]

def union(x, y):
    x = find_(x)
    y = find_(y)
    if x == y:
        return
    elif x > y:
        p[x] = y
    else:
        p[y] = x

def cal_d(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

N = int(input())
arr = [list(map(float, input().split())) for _ in range(N)]
p = [x for x in range(N+1)]

queue = []
for i in range(N-1):
    for j in range(i+1, N):
        heapq.heappush(queue, [cal_d(arr[i], arr[j]), i, j])
print(queue)

cnt = 0
result = 0
while cnt < N-1:
    d, p1, p2 = heapq.heappop(queue)
    if find_(p1) != find_(p2):
        union(p1, p2)
        cnt += 1
        result += d
print(f"{result:.2f}")