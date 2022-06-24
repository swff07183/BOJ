import sys
input = lambda: sys.stdin.readline().rstrip()

def cook(cnt, check=0, sin=1, theun=0):
    global result
    if check > 0 and result > abs(sin-theun):
        result = abs(sin-theun)
    if cnt == N:
        return
    
    cook(cnt+1, check+1, sin*arr[cnt][0], theun+arr[cnt][1])
    cook(cnt+1, check, sin, theun)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = int(1e10)

cook(0)
print(result)