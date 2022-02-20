N = int(input())

p = list(map(int, input().split()))

p.sort()
for i in range(1, N):
    p[i] += p[i-1]
print(sum(p))