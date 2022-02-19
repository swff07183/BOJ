import sys

sys.stdin = open("input.txt")


def get_next_arr(pattern):
    # preprocessing
    len_p = len(pattern)
    arr = [0 for x in range(len_p)]
    j = 0
    for i in range(1, len_p):
        while j > 0 and pattern[i] != pattern[j]:
            j = arr[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            arr[i] = j


    return arr



def kmp(pattern, text):
    len_p = len(pattern)
    len_t = len(text)

    next_arr = get_next_arr(pattern) # next 배열 계산

    idx_p = 0 # pattern 의 index
    idx_t = 0 # text 의 index
    pos_p = [] # p가 나타난 위치

    for idx_t in range(len_t):
        while idx_p > 0 and pattern[idx_p] != text[idx_t]:
            idx_p = next_arr[idx_p-1]

        if pattern[idx_p] == text[idx_t]:
            idx_p += 1
            if idx_p == len_p:
                pos_p.append(idx_t - len_p + 2)
                idx_p = next_arr[idx_p-1]

    return pos_p

text = input()
pattern = input()

result = kmp(pattern, text)

print(len(result))
for pos in result:
    print(pos, end=" ")
