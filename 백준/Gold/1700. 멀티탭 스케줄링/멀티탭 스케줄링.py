import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
arr = list(map(int, input().split()))

state = []
ans = 0

for i in range(K):
    if len(state) < N:
        if arr[i] not in state:
            state.append(arr[i])
    else:
        if arr[i] not in state:
            tmp = {}

            for j in range(K-1, i, -1):
                tmp[arr[j]] = j
            tmp = sorted([[k, tmp.get(k, 101)] for k in state], key=lambda x: -x[1])
            state.pop(state.index(tmp[0][0]))
            state.append(arr[i])
            # print("pop!", tmp[0][0], tmp)
            ans += 1
    # print(f"i:{i}, arr[i]: {arr[i]} state: {state}")
print(ans)

            