import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline

def cal_distance(data):
    result = int(data[0])
    for idx in range(1, 2*N-1, 2):
        oper = data[idx]
        n2 = int(data[idx+1])
        if oper == '+':
            result += n2
        elif oper == '-':
            result -= n2
        elif oper == '*':
            result *= n2
    return result

def dfs(i, j, total):
    global max_result, min_result
    if i == N-1 and j == N-1:
        result = cal_distance(total)
        max_result = max(max_result, result)
        min_result = min(min_result, result)
    for d in range(2):
        ni = i + di[d]
        nj = j + dj[d]
        if (0<=ni<N and 0<=nj<N):
            dfs(ni, nj, total + [arr[ni][nj]])


di = [1, 0]
dj = [0, 1]

N = int(input())

max_result = -5**N
min_result = 5**N

arr = [input().split() for _ in range(N)]

dfs(0, 0, [arr[0][0]])
print(max_result, min_result)
