# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root.left and not root.right:
            return True
        if (root.left or root.right) and not (root.left and root.right):
            return False
        if root.left.val != root.right.val:
            return False
        
        def search(left:Optional[TreeNode], right:Optional[TreeNode]):
            if not left and not right:
                return True
            if (left or right) and not (left and right):
                return False
            if left.val != right.val:
                return False
            return search(left.left, right.right) and search(left.right, right.left)
        
        return search(root.left, root.right)
