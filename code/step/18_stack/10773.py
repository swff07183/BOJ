N = int(input())
numbers = []

for _ in range(N):
    num = int(input())
    if num==0:
        numbers.pop()
    else:
        numbers.append(num)
print(sum(numbers))