arr = list(map(int, input().split()))

def dfs(cur, prv1, prv2, total=0):
    global result
    if total + (10-cur) < 5:
        return
    if cur == 10:
        if total >= 5:
            result += 1
        return
    for i in range(1, 6):
        if prv1 == i and prv2 == i:
            continue
        if arr[cur] == i:
            dfs(cur+1, prv2, i, total + 1)
        else:
            dfs(cur+1, prv2, i, total)


result = 0
dfs(0, 0, 0)
print(result)