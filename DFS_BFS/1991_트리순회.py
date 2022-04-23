import sys

def preorder(root):
    # root -> left -> right 순 

    if root !='.':
        print(root,end='') # root
        preorder(tree[root][0]) # left 
        preorder(tree[root][1]) # right 
    
def inorder(root):
    # left -> root -> right 

    if root !='.':
        inorder(tree[root][0]) # left 
        print(root,end='') # root
        inorder(tree[root][1]) # right 

def postorder(root):
    # left -> right -> root 

    if root != '.':
        postorder(tree[root][0]) # left 
        postorder(tree[root][1]) # right 
        print(root,end='') # root


n = int(input())
tree = {}

for _ in range(n):
    root, left, right = sys.stdin.readline().split()
    tree[root] = [left,right]


preorder('A')
print()
inorder('A')
print()
postorder('A')


## 후기 
# dictionary를 사용해 root를 만들 수 있었다. 짱 
# preorder, inorder, postorder 개념 복습 할 수 있었다. 짱 