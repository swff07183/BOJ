"""
밑 줄
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

def sort_(c):
    if c[1][0].islower():               #  소문자면 정렬
        return -10000
    elif c[1][0].isupper():             # 대문자면 역순으로 정렬
        return -c[0]

N, M = map(int, input().split())

arr = [[i, input()] for i in range(N)]  # arr 받을떄 인덱스도 같이 넣기
arr.sort(key=lambda x: (sort_(x)))      # 정렬

cnt = 0
for c in arr:
    cnt += len(c[1])

i = 0
while cnt < M:
    if arr[i][0] != 0:
        arr[i][1] = '_' + arr[i][1]
        cnt += 1
    i = (i + 1) % N
        
arr.sort()
ans = ''.join([arr[x][1] for x in range(N)])
print(ans)
