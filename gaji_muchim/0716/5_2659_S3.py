"""
십자카드 문제
"""

def get_clock_num(card):
    """
    카드 4개 중에 시계방향으로 돌면서 가장 작은 값(시계수) 찾기
    0 1 2 3
    1 2 3 0
    2 3 0 1
    3 0 1 2
    """
    ret = 10000
    for i in range(4):
        tmp = ''
        for j in range(4):
            idx = (i+j) % 4
            tmp += card[idx]
        ret = min(ret, int(tmp))
    return ret
    

def make_card(cnt, tmp):
    """
    카드만들기
    9^4
    """
    if cnt == 4:
        tmp = get_clock_num(tmp)
        clock_num.append(tmp)
        return
    for i in range(1, 10):
        make_card(cnt+1, tmp + [str(i)])


clock_num = []
make_card(0, [])
clock_num = sorted(list(set(clock_num)))

arr = input().split()
ans = clock_num.index(get_clock_num(arr)) + 1
print(ans)