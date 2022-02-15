import sys
input = sys.stdin.readline


def merge_sort(num_list) :
  # 생략
def merge(nums1, nums2) :
  # 생략

  
num_list = []

N = int(input())

for _ in range(N) :
    num = int(input())
    num_list.append(num)

sorted_list = merge_sort(num_list) # 리스트 오름차순 정렬

list_sum = 0 # 합계를 저장할 변수
dict_count = {} # 빈도 수를 저장할 변수. key: 자료, value: 빈도 수
for num in sorted_list : # 리스트를 순회하면서 합계와 빈도수를 구한다.
    list_sum += num
    dict_count[num] = dict_count.get(num, 0) + 1

# 딕셔너리를 value값을 기준으로 내림차순 정렬한다.
mode_list = sorted(dict_count.items(), key=lambda x: x[1], reverse=True)

print("%.0f" % (list_sum / N)) # 1. 산술평균
print(sorted_list[N//2]) # 2. 중앙값

# 최빈값
if len(mode_list) == 1 : # 자료의 종류가 하나일때는 그 자료 출력
    print(mode_list[0][0])
elif mode_list[0][1] == mode_list[1][1] : # 만약 빈도수가 같은 자료가 여러개라면 두번째로 큰 자료 출력
    print(mode_list[1][0])
else :
    print(mode_list[0][0]) # 아니라면 제일 많이 나온 값 출력

print(sorted_list[-1] - sorted_list[0]) # 4. 범위
