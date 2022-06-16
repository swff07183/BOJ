import sys
input = lambda : sys.stdin.readline().rstrip()

def bin_search():
    s = 1
    e = arr[-1] - 1

    while s <= e:
        mid = (s + e) // 2
        tmp = arr[0]
        cnt = 1
        for i in range(1, N):
            if arr[i]-tmp >= mid:
                cnt += 1
                tmp = arr[i]
        if cnt >= C:
            s = mid + 1
        else:
            e = mid - 1
    return e        
    

N, C = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(int(input()))

arr.sort()
result = bin_search()
print(result)