class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
    
            left_depth = dfs(root.left)
            right_depth = dfs(root.right)
            
            return max(left_depth, right_depth) + 1
        return dfs(root)