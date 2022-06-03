from collections import deque

def solution(cacheSize, cities):
    answer = 0
    q = []
    
    for city in cities:
        city = city.lower()
        if city in q:
            q.pop(q.index(city))
            q.append(city)
            answer += 1
        else:
            q.append(city)
            while len(q) > cacheSize:
                q.pop(0)
            answer += 5
            
    return answer