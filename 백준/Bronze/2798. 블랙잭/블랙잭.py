n, m = tuple(map(int, input().split()))

cardList = list(map(int, input().split()))

blackJack = 0

for i in range(n-2) :
    for j in range(i+1, n-1) :
        for k in range(j+1, n):
            cardSum = cardList[i]+cardList[j]+cardList[k]
            if 0 <= m-cardSum < m - blackJack :
                blackJack = cardSum

print(blackJack)
