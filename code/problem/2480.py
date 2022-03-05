a, b, c = map(int, input().split())


if a==b==c :
    result = 10000+ 1000*a
elif a==b or a==c:
    result = 1000 + 100 * a
elif b==c:
    result = 1000 + 100 * b
else:
    result = max(a, b, c) * 100

print(result)
