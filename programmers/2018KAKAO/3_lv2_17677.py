def file_name(files):
    result = []
    
    for file in files:
        n, t = 0, 0
        while not file[n].isdigit():
            n += 1
            t += 1
        try:
            while file[t].isdigit():
                t += 1
        except:
            pass
        head = file[:n]
        number = file[n:t]
        tail = file[t:]
    
        result.append([file, head.lower(), int(number), tail])
    
    return result
    
    

def solution(files):
    answer = []
    
    files = file_name(files)
    
    files.sort(key=lambda x: (x[1], x[2]))
    
    answer = [x[0] for x in files]
        
    
    return answer