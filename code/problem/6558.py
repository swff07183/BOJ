import sys
input = sys.stdin.readline

def prime_sum(n):
    for i in range(2, n):
        if i > n/2:
            break
        if sieve[i] and sieve[n-i]:
            return i, n-i
    return 0, 0

MAX_LEN = 1000010

sieve = [True for _ in range(MAX_LEN)]

sieve[0] = False
sieve[1] = False

for i in range(1, MAX_LEN):
    if i * i > MAX_LEN:
        break
    if not sieve[i]:
        continue
    for j in range(i*i, MAX_LEN, i):
        sieve[j] = False

while True:
    n = int(input())
    if not n:
        break
    
    x, y = prime_sum(n)
    if x and y:
        print(f"{n} = {x} + {y}")
    else:
        print("Goldbach's conjecture is wrong.")