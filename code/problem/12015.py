import sys
input = sys.stdin.readline

def bin_search(n):
    start = 0
    end = len(lcs)
    while start <= end:
        mid = (start + end) // 2
        if lcs[mid] < n:
            start = mid+1
        else:
            end = mid-1

    return start
    
        

lcs = []

N = int(input())
arr = list(map(int, input().split()))

lcs.append(arr[0])

for i in range(1, N):
    if arr[i] > lcs[-1]:
        lcs.append(arr[i])
    else:
        idx = bin_search(arr[i])
        lcs[idx] = arr[i]


print(len(lcs))