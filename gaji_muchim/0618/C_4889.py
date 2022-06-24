import sys
input = lambda : sys.stdin.readline().rstrip()

def stable(word):
    stack = []
    # 일단 word 한번 순회하면서 {} 있으면 다 지워주기
    for c in word:
        if c == '}' and len(stack) and stack[-1]=='{':
            stack.pop()
        else:
            stack.append(c)
    """
    
    } }
    { {
    } {
    """
    # 그럼 남는 패턴은 }}, {{, } { 가 된다.

    result = 0
    for i in range(1, len(stack), 2):
        if stack[i]==stack[i-1]:
            # } } , { { => {}
            result += 1
        else:
            # } { => {}
            result += 2
    return result
        
tc = 1
while True:
    word = input()
    if word[0] == '-':
        break
    
    result = stable(word)
    print(f'{tc}. {result}')
    tc += 1