import sys

while True:
    try:
        a = sorted(list(input()))
        b = sorted(list(input()))
    except:
        break
    tmp = 0
    result = ""
    len_a = len(a)
    len_b = len(b)
    for i in range(len_a):
        for j in range(tmp, len_b):
            if a[i]==b[j]:
                result += a[i]
                tmp = j+1
                break

    print(result)