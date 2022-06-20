def solution(info, edges):
    answer = 0

    def recur(sheep, wolf, node, cand=[]):
        if sheep <= wolf:
            return sheep
        ret = sheep
        for nxt in cand:
            if v[nxt]:
                continue
            v[nxt] = True
            if info[nxt] == 0:
                ret = max(ret, recur(sheep+1, wolf, nxt, cand + graph[nxt]))
            else:
                ret = max(ret, recur(sheep, wolf+1, nxt, cand + graph[nxt]))
            v[nxt] = False
        return ret
    
    graph = [[] for _ in range(len(info))]
    for s, e in edges:
        graph[s].append(e)
    v = [False for _ in range(len(info))]
    if info[0] == 0:
        answer = recur(1, 0, 0, graph[0])
        
    return answer