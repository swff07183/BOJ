N, K = map(int, input().split())

sieve = [True for _ in range(N+1)]

sieve[0] = False
sieve[1] = False
cnt = 0

for i in range(2, N+1):
    if not sieve[i]:
        continue
    for j in range(i, N+1, i):
        if sieve[j]:
            sieve[j] = False
            cnt += 1
            if cnt == K:
                print(j)
                break
