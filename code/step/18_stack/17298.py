import sys
sys.stdin = open("input.txt")

def NGE(nums, n):
    result = [-1 for _ in range(n)]
    for i in range(n):
        s1 = []

        for j in range(n-1, i, -1):
            s1.append(nums[j])
        while len(s1) and result[i] == -1:
            nn = s1.pop()
            if nn > nums[i]:
                result[i] = nn


    return result

N = int(input())

numbers = list(map(int, input().split()))

print(*NGE(numbers, N))