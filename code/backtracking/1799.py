import sys
input = sys.stdin.readline

def bound(cur):
    result = 0
    for d in range(cur, 2*N-1):
        for i in range(N):
            j = i+N-1-d
            if (0<=i<N and 0<=j<N) and arr[i][j] and not v2[i+j]:
                result += 1
                break
    return result
            

def recur(cur, total):
    global result
    if cur == 2*N-1:
        result = max(result, total)
        return
    ub = bound(cur)
    if total + ub <= result:
        return

    for i, j in pos[cur]:
        if not v2[i+j]:
            v2[i+j]=True
            recur(cur+1, total+1)
            v2[i+j]=False
    recur(cur+1, total)


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

v1 = [False for _ in range(2*N)]
v2 = [False for _ in range(2*N)]

pos = {
    x:[] for x in range(2*N-1)
}
cnt = 0

for i in range(N):
    for j in range(N):
        if arr[i][j]:
            pos[i-j+N-1].append((i, j))
            cnt += 1


result = 0
recur(0, 0)

print(result)