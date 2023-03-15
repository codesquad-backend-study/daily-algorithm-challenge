# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = 0

        def dfs(node):
            nonlocal max_diameter # nonlocal : 내부함수에서 외부함수의 변수를 변경 할 수 있게 함.

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            max_diameter = max(max_diameter, left + right)

            return max(left, right) + 1

        dfs(root)
        return max_diameter
