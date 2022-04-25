S = input()
tmp = S[0]
cnt = 1
for c in S[1:]:
    if c != tmp:
        cnt += 1
        tmp = c

print(cnt//2)