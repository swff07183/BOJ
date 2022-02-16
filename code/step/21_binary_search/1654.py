K, N = list(map(int, input().split()))

line_list = []

for _ in range(K):
    line_list.append(int(input()))

start = 1
end = max(line_list)

while start <= end :
    mid = (start + end) // 2
    total = 0
    for line in line_list:
        total += line // mid
    if total >= N:
        start = mid + 1
    else:
        end = mid - 1
print(end)