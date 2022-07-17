"""
단축키 지정
"""
N = int(input())
arr = [list(map(list, input().split())) for _ in range(N)]
hotkey = {}

for i in range(len(arr)):
    flag = False
    # 일단 단어의 첫글짜부터 확인
    for j in range(len(arr[i])):
        if not hotkey.get(arr[i][j][0].lower()):
            hotkey[arr[i][j][0].lower()] = True
            arr[i][j][0] = '[' + arr[i][j][0] + ']'
            flag = True
            break
    
    # 아님 한글자씩 확인
    if not flag:
        for j in range(len(arr[i])):
            for k in range(1, len(arr[i][j])):
                if not hotkey.get(arr[i][j][k].lower()):
                    hotkey[arr[i][j][k].lower()] = True
                    arr[i][j][k] = '[' + arr[i][j][k] + ']'
                    flag = True
                    break
            if flag:
                break
ans = []
for words in arr:
    tmp = []
    for s in words:
        tmp.append(''.join(s))
    ans.append(' '.join(tmp))

for word in ans:
    print(word)