class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 반대되는 애들을 넣어줘서 같은지 비교하면 되구나..
# 이젠 놀랍지도 않다.
def isSymmetric(root):
    def isMirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return left.val == right.val and isMirror(left.left, right.right) and isMirror(left.right, right.left)
    
    if not root:
        return True
    return isMirror(root.left, root.right)

node1 = TreeNode(3)
node2 = TreeNode(4)
node3 = TreeNode(2, node1, node2)
node4 = TreeNode(4)
node5 = TreeNode(3)
node6 = TreeNode(2, node4, node5)
node7 = TreeNode(1, node3, node6)
print(isSymmetric(node7))