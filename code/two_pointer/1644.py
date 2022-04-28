import sys
input = sys.stdin.readline

def is_prime(n):
    if n < 2 :
        return False
    for i in range(2, n):
        if i**2 > n:
            break
        if n%i == 0:
            return False
    return True

def sum_prime():
    l, r = 0, 0
    tmp = 2
    result = 0
    len_p = len(prime_numbers)
    while l < len_p and r < len_p:
        if tmp < N:
            r += 1
            if r >= len_p:
                break
            tmp += prime_numbers[r]
        elif tmp >= N:
            if tmp == N:
                result += 1
            tmp -= prime_numbers[l]
            l += 1
    return result


N = int(input())
prime_numbers = []
for i in range(2, N+1):
    if is_prime(i):
        prime_numbers.append(i)
result = sum_prime()
print(result)
