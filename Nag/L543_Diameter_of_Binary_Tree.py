# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        answer = 0
        list = []

        if not root:
            return answer
        if not root.left and not root.right:
            return answer
            
        def searchToEnd(node: [TreeNode]):
            leftDepth = 0
            rightDepth = 0

            if node.left:
                leftDepth = searchToEnd(node.left) + 1
            if node.right:
                rightDepth = searchToEnd(node.right) + 1
            if not node.left and not node.right:    
                return 0
            list.append(leftDepth + rightDepth)
            return max(leftDepth, rightDepth)
        searchToEnd(root)
        return max(list)
        
