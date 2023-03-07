# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        pointer = root
        if not root:
            return 0
        answer = self.move(pointer)
        
        return answer

    def move(self, node):
        count = 1
        leftCount = 0
        rightCount = 0

        if node.left:
            leftCount = self.move(node.left) + 1
        if node.right:
            rightCount = self.move(node.right) + 1
        
        return max([count, leftCount, rightCount])
