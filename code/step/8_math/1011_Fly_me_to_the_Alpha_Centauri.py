def alpha_centauri(d) :
    i = 1
    while(True) :
        if i%2 == 0 :
            d-= i//2
        else :
            d-= i//2+1 
        if d <= 0 :
            break
        i+=1
    
    return i

T = int(input())

for i in range(T) :
    x, y = tuple(map(int, input().split()))
    distance = y-x
    print(alpha_centauri(distance))