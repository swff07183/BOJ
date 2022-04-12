import sys
input = sys.stdin.readline

MAX_NUM = 100000


class max_heap:
    def __init__(self):
        self.arr = [0 for _ in range(MAX_NUM+1)]
        self.cnt = 0

    def push(self, x):
        self.arr[self.cnt+1] = x
        child = self.cnt+1
        parent = child // 2

        while child > 1 and self.arr[parent] < self.arr[child]:
            self.arr[parent], self.arr[child] = self.arr[child], self.arr[parent]
            child = parent
            parent = child // 2
        self.cnt += 1

    def pop(self):
        if self.cnt==0:
            return 0
        else:
            # 무조건 1번 노드 출력,
            result = self.arr[1]
            # 마지막 노드의 값 1번 노드로 올리고
            self.arr[1] = self.arr[self.cnt]
            # 마지막 노드 값 0으로 바꾸기
            self.arr[self.cnt] = 0

            parent = 1
            while True:
                lc = parent*2
                rc = parent*2+1
                if not (lc<=MAX_NUM and rc<=MAX_NUM):
                    break
                if self.arr[parent] >= self.arr[lc] and self.arr[parent] >= self.arr[rc]:
                    break
                if self.arr[rc] > self.arr[lc]:
                    self.arr[parent], self.arr[rc] = self.arr[rc], self.arr[parent]
                    parent = rc
                else:
                    self.arr[parent], self.arr[lc] = self.arr[lc], self.arr[parent]
                    parent = lc
                        
            return result

    def __str__(self):
        return str(self.arr[:self.cnt+1])

N = int(input())
h = max_heap()

for _ in range(N):
    num = int(input())
    if num:
        h.push(num)
    else:
        print(h.pop())