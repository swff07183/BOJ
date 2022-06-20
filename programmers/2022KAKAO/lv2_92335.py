def solution(n, k):
    answer = 0
    
    def make_(n, k):
        result = ''
        while n:
            result = str(n % k) + result
            n = n // k
        return result

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, n):
            if i*i > n:
                break
            if n%i == 0:
                return False
        return True
    
    num = make_(n, k)
    
    tmp = ''
    for i in range(len(num)):
        if num[i] == '0':
            if tmp:
                answer += int(is_prime(int(tmp)))
                tmp = ''
        else:
            tmp += num[i]

    if tmp:
        answer += int(is_prime(int(tmp)))

    
    return answer