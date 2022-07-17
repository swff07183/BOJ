"""
어떤 문자열
[팰린드롬 아닌부분] [팰린드롬인 부분]
요걸 팰린드롬으로 만들꺼면
[팰린드롬 아닌부분] [팰린드롬인부분] [팰린드롬 아닌부분::-1]
"""

import sys
input = lambda: sys.stdin.readline().rstrip()

def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

S = input()
if is_palindrome(S):
    print(len(S))
    exit()
tmp = ''
for c in S:
    tmp += c
    S_tmp = S + tmp[::-1]
    if is_palindrome(S_tmp):
        print(len(S_tmp))
        break