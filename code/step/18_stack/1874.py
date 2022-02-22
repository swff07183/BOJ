import sys
sys.stdin = open("input.txt")


class Stack:
    def __init__(self):
        self.arr = []
        self.top = -1

    def __len__(self):
        return self.top + 1

    def push(self, value):
        self.arr.append(value)
        self.top += 1

    def pop(self):
        if self.top != -1:
            self.top -= 1
            return self.arr.pop()
        else:
            return None

    def peek(self):
        if self.top != -1:
            return self.arr[-1]
        else:
            return None


def is_pos_seq(N, seq):
    s1 = Stack()
    idx = 0
    num = 1
    op = []

    while num <= N + 1 and idx < N:
        if s1.peek() != seq[idx] and num <= N:
            s1.push(num)
            num += 1
            op.append('+')
        else:
            s1.pop()
            idx += 1
            op.append('-')
    if len(s1) > 0:
        return None
    else:
        return op



N = int(input())

seq = []

for _ in range(N):
    seq.append(int(input()))

result = is_pos_seq(N, seq)

if result:
    for o in result:
        print(o)
else:
    print("NO")


