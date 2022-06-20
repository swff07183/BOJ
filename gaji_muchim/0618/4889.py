import sys
input = lambda : sys.stdin.readline().rstrip()

def stable(word):
    stack = []
    for c in word:
        if c == '}' and len(stack) and stack[-1]=='{':
            stack.pop()
        else:
            stack.append(c)
            
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