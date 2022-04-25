def eval_(eq):
    nums = eq.split('+')
    total = 0
    for n in nums:
        total += int(n)
    return total

arr = input().split('-')
result = eval_(arr[0])
for eq in arr[1:]:
    result -= eval_(eq)
print(result)