"""
볼 모으기
R R R R R [B] B R R B R R B B B R B R R R
           ->   R R   R R       R   R R R
"""

N = int(input())
arr = input()
ans = N+1

for _ in range(2):
    arr = arr[::-1]
    for b in ['R', 'B']:
        i = arr.find(b)
        tmp = len(arr[i:].replace(b, ''))
        ans = min(ans, tmp)

print(ans)