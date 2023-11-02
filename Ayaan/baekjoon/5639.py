import sys
sys.setrecursionlimit(10**5)

# 트리 클래스 만들어서 사용해보기
class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, key):
        if self.val > key:
            if self.left is None:
                self.left = Tree(key)
            # left가 있을 경우 left에 다시 insert
            else:
                self.left.insert(key)
        else:
            if self.right is None:
                self.right = Tree(key)
            # right가 있을 경우 right에 다시 insert
            else:
                self.right.insert(key)


preorder = []
while True:
    try:
        preorder.append(int(input()))
    except:
        break

tree = Tree(preorder[0])
for i in range(1, len(preorder)):
    tree.insert(preorder[i])


def postorder(root):
    if root.left:
        postorder(root.left)
    if root.right:
        postorder(root.right)
    print(root.val)


postorder(tree)
