N = int(input())

arr = sorted(list(map(int, input().split())), reverse=True)

score = 0
slime = arr[0]

for i in range(1, N):
    score += slime * arr[i]
    slime += arr[i]
print(score)