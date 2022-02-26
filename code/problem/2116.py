import sys
sys.stdin = open("input.txt")

"""
A F [BCDE]
B D [ACEF]
C E [ABDF]
"""

pair = {
    0: 5,
    1: 3,
    2: 4,
    3: 1,
    4: 2,
    5: 0
}

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_sum = 0

for i in range(6):
    top = arr[0][i]
    total = 0
    for j in range(N):
        bottom = top
        bottom_idx = arr[j].index(bottom)
        top = arr[j][pair[bottom_idx]]
        if top + bottom == 11:
            max_num = 4
        elif top == 6 or bottom == 6:
            max_num = 5
        else:
            max_num = 6
        total += max_num
    if max_sum < total:
        max_sum = total
print(max_sum)