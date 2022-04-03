import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, depth):
    global cnt
    if node==-1:                    # 노드가 -1이면 리턴
        return
    dfs(tree[node][0], depth+1)     # 왼쪽 자식 노드 부터
    width[depth].append(cnt)        # 열 번호 추가하고 1 증가
    cnt+=1
    dfs(tree[node][1], depth+1)     # 오른쪽 자식 노드
    

N = int(input())
tree = [[] for _ in range(N+1)]

cnt = 1                             # 노드 열 번호
width = [[] for _ in range(N+1)]    # 깊이 별로 노드 열 번호 저장

parent = [x for x in range(N+2)]    # 해당 노드의 부모 저장할 리스트
for _ in range(N):
    p, l, r = map(int, input().split())
    parent[l] = p                   # 부모 노드 정보 저장
    parent[r] = p
    tree[p] = [l, r]                # 트리 만들기

root = 1
while parent[root] != root:
    root = parent[root]  # 루트 찾기

dfs(root, 1)

result = (0, -1)  # (레벨, 최대값)
for i in range(1, len(width)):
    if not width[i]:
        break
    tmp = max(width[i]) - min(width[i])+1
    if tmp > result[1]:
        result = (i, tmp)

print(*result)