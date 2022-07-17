import sys
input = lambda: sys.stdin.readline().rstrip()

DIV_NUM = int(1e9) + 7

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

div_a = [0 for _ in range(7)]           # A의 요소들을 7로 나누ㄴ 나머지로 그룹

for i in range(N):
    div_a[A[i] % 7] += 1

is_zero = [False for _ in range(7)]     # 해당하는 그룹이 연산중에 0으로 바뀌는지 확인
plus = 0                                # 연산 수행한 합 저장할 변수

for i in range(M):
    cnt, zero_cnt = 0, 0
    plus_tmp = plus + B[i]              # 일단 연산 결과에 넣고 개수 세보기
    tmp = is_zero[:]
    for j in range(7):
        if is_zero[j] or not div_a[j]:  # 이미 0이 되었거나 요소가 없다면 그냥 넘기기
            continue

        cnt += div_a[j]                 # 해당하는 개수 더해주고
        if (j + plus_tmp) % 7 == 0:     # 이번 연산까지 했을때 0이되면
            zero_cnt += div_a[j]        # 0이 된 개수 늘려주고
            tmp[j] = True               # tmp True로 바꿔주기
            
    if zero_cnt != cnt:                 # 0이된 개수랑 전체 개수랑 같지 않다면
        is_zero = tmp[:]                # 해당 연산 이후 결과 is_zero에 반영
        plus = plus_tmp                 # 누적합에 더해주기

result = []

for i in range(N):
    if is_zero[A[i] % 7]:       # 만약 이거 중간에 없어지는 녀석이다 하면
        continue                # 결과에 넣지 않기
    result.append((A[i] + plus) % DIV_NUM)

print(len(result))
print(*result)