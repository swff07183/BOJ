"""
기차가 어둠을 헤치고 은하수를
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

train = [0 for _ in range(N+1)]

for _ in range(M):
    oper = list(map(int, input().split()))

    if oper[0] == 1:
        i, x = oper[1], oper[2]
        train[i] = train[i] | (1 << (x-1))

    elif oper[0] == 2:
        i, x = oper[1], oper[2]
        train[i] = train[i] & ~(1 << (x-1))

    elif oper[0] == 3:
        i = oper[1]
        # train[i] = (train[i] << 1) % (1 << 20)
        train[i] = (train[i] << 1) & ((1 << 20) - 1)

    elif oper[0] == 4:
        i = oper[1]
        train[i] = train[i] >> 1

ans = len(set(train[1:]))
print(ans)