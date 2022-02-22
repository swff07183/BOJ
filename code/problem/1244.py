import sys
sys.stdin = open("input.txt")


def swap(n):
    return int(not n)


def switch_man(num, status, N):
    i = num
    while i <= N:
        status[i] = swap(status[i])
        i += num


def switch_woman(num, status, N):
    start = num
    end = num
    while 1 <= start <= N and 1 <= end <= N:
        if status[start] == status[end]:
            a = swap(status[start])
            status[start] = a
            status[end] = a
            start -= 1
            end += 1
        else:
            return

N = int(input())    # 스위치 개수
status = [0] + list(map(int, input().split()))    # 스위치 상태

M = int(input())    # 학생 수
for i in range(M):
    gender, num = map(int, input().split())
    if gender == 1:
        switch_man(num, status, N)
    elif gender == 2:
        switch_woman(num, status, N)

for i in range(1, len(status)):
    print(status[i], end=" ")
    if i % 20 == 0:
        print()
