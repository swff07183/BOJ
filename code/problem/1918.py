oper = {
    # 연산자 우선순위
    # key: 연산자, value: [icp isp]
    "+": [1, 1],
    "-": [1, 1],
    "*": [2, 2],
    "/": [2, 2],
    "(": [0, 3],
}


def in_to_post(ex):
    stack=[]
    result = ""
    for e in ex:
        if e in oper:
            # 우선순위 비교해서 낮거나 같은것들 빼서 결과에 넣기
            while len(stack) > 0 and oper[e][1] <= oper[stack[-1]][0]:
                result += stack.pop()
            stack.append(e)         # 맨 위에있는게 나보다 우선순위 클때 그냥 넣기
        elif e == ")":              # 닫는 괄호가 나왔을 떄
            while len(stack) > 0:
                temp = stack.pop()  # 하나 빼보기
                if temp == "(" :    # 여는 괄호다?
                    break           # 그럼 안더하고 다음거 확인
                result += temp      # 여는 괄호 아니면 결과에 다 더하기
        else:
            result += e             # 숫자면 다 더하기
    while len(stack) > 0:
        result += stack.pop()
    return result



ex = input()
postfix = in_to_post(ex)
print(postfix)
