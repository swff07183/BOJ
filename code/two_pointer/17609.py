import sys
input = sys.stdin.readline

def is_s_palindrome(word):
    if is_palindrome(word):
        return 0
    else:
        l, r = 0, len(word)-1
        cnt = 0
        while l <= r and cnt <= 1:
            if word[l] == word[r]:
                l += 1
                r -= 1
            else:
                if is_palindrome(word[l+1:r+1]):
                    return 1
                if is_palindrome(word[l:r]):
                    return 1
                return 2

def is_palindrome(word):
    if word == word[::-1]:
        return True
    return False

result = []
N = int(input())
for _ in range(N):
    print(is_s_palindrome(input().rstrip()))