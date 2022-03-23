from collections import deque

def bfs(start, end):
    queue = deque()
    queue.append(start)
    v = [-1 for _ in range(100001)]
    v[start] = 0

    while queue:
        for _ in range(len(queue)):
            pos = queue.popleft()
            if pos == end:
                return v[pos]
            if 2*pos <= 100000 and v[pos*2] == -1:
                queue.append(pos*2)
                v[pos*2] = v[pos]
            if pos-1 >= 0 and v[pos-1] == -1:
                queue.append(pos-1)
                v[pos-1] = v[pos] + 1
            if pos+1 <= 100000 and v[pos+1] == -1:
                queue.append(pos+1)
                v[pos+1] = v[pos] + 1


N, K = map(int, input().split())

result = bfs(N, K)
print(result)