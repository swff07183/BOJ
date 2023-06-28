import sys

input = sys.stdin.readline

class Stack:
    # stack이 최초 생성 될 때 필요한 정보들
    # stack의 크기를 기본 값으로 받아와야 한다.
    def __init__(self):
        # stack의 크기
        # stack을 저장할 자료 구조
        # 최초 stack 생성 시 각 위치에는 값이 없다.
        self.arr = []
        # stack의 최상단
        self.top = -1
        self.size = 0

    def empty(self):
        if not self.size:
            return 1
        else:
            return 0


    # stack의 추가 연산 == push
    # top 위치에 값을 입력
    def push(self, n):
        self.top += 1
        self.size += 1
        self.arr.append(n)

    def pop(self):
        if self.size != 0:
            result = self.arr.pop()
            self.top -= 1
            self.size -= 1
            return result
        else :
            return -1

    def peek(self):
        if self.size != 0:
            return self.arr[self.top]
        else :
            return -1

s1 = Stack()
N = int(input())
for _ in range(N):
    oper = input().split()
    if oper[0] == "push":
        s1.push(oper[1])
    elif oper[0] == "top":
        print(s1.peek())
    elif oper[0] == "size":
        print(s1.size)
    elif oper[0] == "pop":
        print(s1.pop())
    elif oper[0] == "empty":
        print(s1.empty())
    