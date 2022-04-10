ip = input().split(':')
if ip[0] == '':
    ip.pop(0)
if ip[-1] == '':
    ip.pop()

z_cnt = 8 - len(ip) + 1
result = ''

for i in range(len(ip)):
    if ip[i] == '':
        for _ in range(z_cnt):
            result += '0000:'
    else:
        result += ip[i].zfill(4)
        result += ':'


print(result[:-1])