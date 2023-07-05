import sys
input = lambda: sys.stdin.readline().rstrip()

class MinHeap:
    def __init__(self):
        self.heap = [0]
        self.size = 0
    
    def is_empty(self):
        return True if len(self.heap) <= 1 else False
    
    def push(self, v):
        self.heap.append(v)
        idx = len(self.heap)-1
        while True:
            parent = idx // 2
            if idx <= 1 or self.heap[parent] < self.heap[idx]:
                break

            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent

    def pop(self):
        if len(self.heap) <= 2:
            return self.heap.pop()

        ret = self.heap[1]
        self.heap[1] = self.heap.pop()
        parent = 1

        while True:
            left_child = parent * 2
            right_child = parent * 2 + 1
            
            if len(self.heap) <= left_child:
                break
            
            elif len(self.heap) == right_child:
                if self.heap[parent] > self.heap[left_child]:
                    self.heap[parent], self.heap[left_child] = self.heap[left_child], self.heap[parent]
                    parent = left_child
                else:
                    break

            else:
                min_v = min(self.heap[parent], self.heap[left_child], self.heap[right_child])
                
                if min_v == self.heap[parent]:
                    break
                elif min_v == self.heap[left_child]:
                    self.heap[parent], self.heap[left_child] = self.heap[left_child], self.heap[parent]
                    parent = left_child
                else:
                    self.heap[parent], self.heap[right_child] = self.heap[right_child], self.heap[parent]
                    parent = right_child
        
        return ret

    def __str__(self):
        return str(self.heap)

heap = MinHeap()

N = int(input())

for _ in range(N):
    x = int(input())
    
    if x == 0:
        if heap.is_empty():
            print(0)
        else:
            print(heap.pop())
    
    else:
        heap.push(x)