import sys
sys.stdin = open("input.txt")

def NGE(nums, n):
    result = [-1 for _ in range(n)]
    s1 = [numbers[n-1]]
    for i in range(n-2, -1, -1):
        try:
            while numbers[i] >= s1[-1]:
                s1.pop()
        except:
            pass
        if len(s1) > 0:
            result[i] = s1[-1]
        s1.append(numbers[i])

    return result

N = int(input())

numbers = list(map(int, input().split()))

print(*NGE(numbers, N))