import sys
input = lambda : sys.stdin.readline().rstrip()

def calc(n1, n2, oper):
    if oper==0:
        return n1 + n2
    elif oper == 1:
        return n1 - n2
    elif oper == 2:
        return n1 * n2
    elif oper == 3:
        if n1 < 0 and n2 > 0:
            return -((-n1) // n2)
        return n1 // n2

def recur(cur, total):
    global max_result, min_result
    if cur == N:
        min_result = min(min_result, total)
        max_result = max(max_result, total)
        return
    for i in range(4):
        if oper[i]:
            oper[i] -= 1
            recur(cur+1, calc(total, numbers[cur], i))
            oper[i] += 1
    

max_result = -1000000001
min_result = 1000000001

N = int(input())
numbers = list(map(int, input().split()))
oper = list(map(int, input().split()))
recur(1, numbers[0])
print(max_result)
print(min_result)