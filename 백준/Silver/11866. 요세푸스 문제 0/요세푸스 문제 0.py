from collections import deque

queue = deque()
result = []

N, K = map(int, input().split())
for i in range(1, N+1):
    queue.append(i)

while len(queue):
    for _ in range(K-1):
        queue.append(queue.popleft())
    result.append(queue.popleft())
print(f"<{', '.join(map(str,result))}>")
