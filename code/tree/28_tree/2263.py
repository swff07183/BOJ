import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def preorder(in_s, in_e, post_s, post_e): 
    # 전위 순회
    # V -> L -> R
    if in_s > in_e:
        return
    root = postorder[post_e]  # 후위순회에서 루트는 맨 마지막
    print(root, end=' ')    # 루트 출력

    idx = pos[root]         # 중위 순회에서 루트 기준 왼쪽 -> 왼쪽 서브트리, 오른쪽 -> 오른쪽 서브트리
    
    preorder(in_s, idx-1, post_s, post_s + (idx-1-in_s))    # 왼쪽 서브트리 순회
    preorder(idx+1, in_e, post_e - (in_e - idx) , post_e-1) # 오른쪽 서브트리 순회

N = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))
pos = [-1 for _ in range(N+1)]
for i in range(N):
    pos[inorder[i]] = i     # 중위순회에서 위치 기록

preorder(0, N-1, 0, N-1)