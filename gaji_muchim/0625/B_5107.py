import sys
input = lambda : sys.stdin.readline().rstrip()

tc = 1
while True:
    N = int(input())
    if N == 0:
        break
    manitto = {}
    v = {}
    for _ in range(N):
        a, b = input().split()
        manitto[a] = b
        v[a] = 0

    cnt = 1
    ans = 0
    for node in manitto:
        if v[node]:
            continue
        while not v[node]:
            v[node] = cnt
            nxt = manitto[node]
            if v[nxt]:
                if v[nxt] == cnt:
                    ans += 1
                break
            node = nxt
        cnt += 1
    print(f'{tc} {ans}')
    tc += 1
