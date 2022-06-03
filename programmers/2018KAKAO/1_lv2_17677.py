def solution(str1, str2):
    def make_alpha_set(word):
        result = []
        tmp = ''
        for c in word.lower():
            if c.isalpha():
                tmp += c
                if len(tmp) >= 2:
                    result.append(tmp)
                    tmp = c
            else:
                tmp = ''
                    
        return result
    
    def similarity(set1, set2):
        i1 = 0
        i2 = 0
        len_set1 = len(set1)
        len_set2 = len(set2)
        set1.sort()
        set2.sort()
        a, b = 0, 0
        while i1 < len_set1 and i2 < len_set2:
            if set1[i1] == set2[i2]:
                tmp = set1[i1]
                cnt1 = 0
                cnt2 = 0
                while i1 < len_set1 and tmp == set1[i1]:
                    cnt1 += 1
                    i1 += 1
                while i2 < len_set2 and tmp == set2[i2]:
                    cnt2 += 1
                    i2 += 1
                a += min(cnt1, cnt2)
                b += max(cnt1, cnt2)
                
            elif set1[i1] > set2[i2]:
                i2 += 1
                b += 1
            else:
                i1 += 1
                b += 1
        b += (len_set1 - i1)
        b += (len_set2 - i2)
        try:
            return (a/b)
        except:
            if a==0:
                return 1
            return 0
                
        
    set1 = make_alpha_set(str1)
    set2 = make_alpha_set(str2)
    
    answer = 0
    answer = int(similarity(set1, set2)*65536)
    return answer