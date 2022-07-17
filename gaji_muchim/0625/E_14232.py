"""
보석도둑
무게가 다 곱해진다
-> k에 딱 맞게 가져와야 하니까
-> 소인수 분해 고
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def is_prime(n):
    # if n < 2:
    #     return False
    for i in range(2, int(n**0.5) + 1):
        if n%i == 0:
            return False
    return True

k = int(input())


result = []
tmp = k
jew = 2
while tmp > 1:
    if jew*jew > k:
        break
    if is_prime(jew):
        while not (tmp%jew):
            tmp //= jew
            result.append(jew)
    jew += 1
if tmp > 1:
    result.append(tmp)
print(len(result))
print(*result)