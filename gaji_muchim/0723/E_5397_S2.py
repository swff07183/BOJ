"""
키로거
BA<<C>D
"""
import sys
sys.stdin = open('input.txt')
input = lambda: sys.stdin.readline().rstrip()

T = int(input())
for _ in range(T):
    oper = input()
    idx = 0
    pw = []
    tmp = []

    for c in oper:
        if c == '<':
            if pw:
                tmp.append(pw.pop())
        elif c == '>':
            if tmp:
                pw.append(tmp.pop())
        elif c == '-':
            if pw:
                pw.pop()
        else:
            pw.append(c)
    while tmp:
        pw.append(tmp.pop())
    ans = ''.join(pw)
    print(ans)
