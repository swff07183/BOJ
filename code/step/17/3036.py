def cal_gcd(a, b):
    if a % b == 0:
        return b
    else :
        return cal_gcd(b, a % b)

N = int(input())


ring_list = list(map(int, input().split()))

base = ring_list[0]

for i in range(1, N):
    gcd = cal_gcd(base, ring_list[i])

    print(f"{base//gcd}/{ring_list[i]//gcd}")