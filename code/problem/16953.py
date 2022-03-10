def bfs(a, b):
    if a > b:
        return -1
    count = 1
    depth = 1
    queue = [a]
    temp = []
    while(count > 0):
        count = 0
        l = len(queue)
        for i in range(l):
            try:
                n = queue.pop(0)
            except IndexError:
                return -1
            n1 = n * 2
            n2 = n * 10 + 1
            # 값 비교
            if n1 == b or n2 == b:
                return depth+1
            if n1 < b:
                queue.append(n1)
                count += 1
            if n2 < b:
                queue.append(n2)
                count += 1
        depth += 1
    return -1


A, B = map(int, input().split())

print(bfs(A, B))