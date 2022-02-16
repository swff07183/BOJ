N, K = list(map(int, input().split()))

coins = []

for _ in range(N):
    coins.append(int(input()))

coins.reverse() # 내림차순 정렬

idx = -1
result = 0
for coin in coins:
    num = K // coin 
    result += num # 결과에 동전 개수 추가
    K -= num*coin # 금액에서 빼주기
print(result)