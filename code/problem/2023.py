def recur(cur, total):
    if not isPrime(total):
        return
    if cur == N:
        print(total)
        return
    for i in range(1, 10):
        recur(cur+1, total*10+i)

def isPrime(num):
    if num==1:
        return False
    for i in range(2, num):
        if i*i > num:
            break
        if num%i == 0:
            return False
    return True

N = int(input())

recur(0, 0)