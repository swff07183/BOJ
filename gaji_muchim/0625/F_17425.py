"""
17427 먼저 풀고 왔음. <- 요것도 구글링함
근데 어렵다
정수론 싫다...

T: 100,000
N: 1,000,000
O(T*N) -> O(N) 으로 줄일수 있는 방법..?

-> 결국 구글링함 근데 생각보다 쉽네 이게되네..?
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

MAX_RANGE = 1000001

f = [1 for x in range(MAX_RANGE)]

for i in range(2, MAX_RANGE):
    for j in range(i, MAX_RANGE, i):
        f[j] += i

g = [0 for x in range(MAX_RANGE)]

for i in range(1, MAX_RANGE):
    g[i] = g[i-1] + f[i]


T = int(input())
for _ in range(T):
    n = int(input())
    print(g[n])