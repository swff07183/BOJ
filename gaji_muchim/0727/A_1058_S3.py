import sys
sys.stdin = open('input.txt')
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
arr = [list(map(lambda x: int(x=='Y'), input())) for _ in range(N)]

ans = 0
for i in range(N):
    tmp = [0 for _ in range(N)]
    for j in range(N):
        if j != i and arr[i][j]:
            tmp[j] = 1
            for k in range(N):
                if k != i and arr[j][k]:
                    tmp[k] = 1
    ans = max(ans, sum(tmp))
print(ans)