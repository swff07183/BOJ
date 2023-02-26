import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
tree = [[] for _ in range(N+1)]
p = [-1 for _ in range(N+1)]
width_d = {}  # key: level, value: list of x

cnt = 1

def preorder(node, level=1):
    if node == -1:
        return
    """
    전위탐색
    L -> V -> R
    """
    global cnt
    l_child, r_child = tree[node]
    
    # 왼쪽 자식 탐색
    preorder(l_child, level+1)
    # 현재 노드 탐색
    width_d[level] = width_d.get(level, []) + [cnt]
    cnt += 1
    # 오른쪽 자식 탐색
    preorder(r_child, level+1)

for _ in range(N):
    node, l_child, r_child = map(int, input().split())
    tree[node] = [l_child, r_child]
    if (l_child != -1):
        p[l_child] = node
    if (r_child != -1):
        p[r_child] = node

# for node in tree:
#     print(node)

root = p[1:].index(-1) + 1    # 루트 찾기

preorder(root)

ans = [-1, -1]  # [레벨, 너비]
for level in sorted(width_d.keys()):
    tmp = max(width_d[level]) - min(width_d[level]) + 1
    if tmp > ans[1]:
        ans = [level, tmp]

print(*ans)