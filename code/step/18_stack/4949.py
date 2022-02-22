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
        else:
            return -1

    def peek(self):
        if self.size != 0:
            return self.arr[self.top]
        else:
            return -1
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False


def is_valid_code(code):
    s1 = Stack()    # 스택 생성

    bracket = {
        ")" : "(",
        "}" : "{",
        "]" : "[",
    }

    for c in code:          # code 한 글자 씩 확인
        if c in bracket.values():
            s1.push(c)      # 만약 글자가 여는 괄호라면 stack에 Push
        elif c in bracket:  # 만약 글자가 닫는 괄호라면
            if not s1.is_empty() and s1.peek() == bracket[c]:
                s1.pop()    # 비어있지 않고, 스택 맨 위의 값과 c와 쌍이 맞으면 pop
            else:
                return 'no'    # 그렇지 않으면 -> 잘못된 코드!!

    return "yes" if s1.is_empty() else "no"



while True:
    code = input()
    if code == ".":
        break

    result = is_valid_code(code)  # 괄호 검사

    print(result)




