import sys
input = lambda: sys.stdin.readline().rstrip()

def is_palindrome(s, e):
    if dp[s][e] != -1:
        return dp[s][e]
    
    if s >= e:
        return 1
    else:
        if arr[s] == arr[e] and is_palindrome(s+1, e-1):
            dp[s][e] = 1
        else:
            dp[s][e] = 0
        return dp[s][e]

N = int(input())
arr = [-1] + list(map(int, input().split()))
dp = [[-1 for _ in range(N+1)] for _ in range(N+1)]
M = int(input())

for _ in range(M):
    s, e = map(int, input().split())
    print(is_palindrome(s, e))