"""
한국이 그리울 땐 서버에 접속하지
처음에 틀림
aa*aa
aa -> False
"""
import sys
input = lambda: sys.stdin.readline().rstrip()

def check(word, patt):
    if len(patt[0]+patt[1]) > len(word):    # 두개 합한거 길이가 짧으면?
        return False
    if patt[0] != word[:len(patt[0])] or patt[1] != word[-len(patt[1]):]:   # 그 다음 접두 접미 가져와서 비교함
        return False
    return True

N = int(input())

patt = input().split('*')       # * 기준으로 분리
for _ in range(N):
    word = input()

    if check(word, patt):       # 체크해서 맞으면
        print("DA")
    else:
        print("NE")
    
