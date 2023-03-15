# 재귀로 푸는 건 너무 어렵다.
# self.변수 이렇게 전역변수를 선언하는 방법을 배웠다.
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def depthOfBinaryTree(root):
            if not root:
                return 0
            
            left_depth = depthOfBinaryTree(root.left)
            right_depth = depthOfBinaryTree(root.right)
            
            self.max_diameter = max(self.max_diameter, left_depth + right_depth)

            return max(left_depth, right_depth) + 1
        
        depthOfBinaryTree(root)
        return self.max_diameter
