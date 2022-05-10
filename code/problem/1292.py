A, B = map(int, input().split())

cnt = 0
result = 0
for i in range(1, B+1):
    for j in range(i):
        cnt += 1
        if A<=cnt<=B:
            result += i

print(result)