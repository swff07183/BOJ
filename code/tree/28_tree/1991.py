import sys
sys.stdin = open('input.txt')

def preorder(node):
    # V -> L -> R
    if node != '.':
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    # L -> V -> R
    if node != '.':
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])

def postorder(node):
    # L -> R -> V
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')

N = int(input())

tree = {}

for _ in range(N):
    node, l_child, r_child = input().split()
    tree[node] = [l_child, r_child]
preorder('A')
print()
inorder('A')
print()
postorder('A')