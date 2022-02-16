def binary_search(t, arr):
    l = 0
    r = len(arr) - 1

    while(l <= r):
        c = (l+r)//2
        if arr[c] == t:
            return 1
        elif arr[c] > t:
            r = c-1
        else:
            l = c+1
    return 0


N = int(input())

numbers = list(map(int, input().split()))

M = int(input())

targets = list(map(int, input().split()))

numbers.sort()

for t in targets:
    print(binary_search(t, numbers))