class Solution:
    def find_depth(self, node):
        if node is None:
            return 0

        return max(self.find_depth(node.left), self.find_depth(node.right)) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        current_diameter = self.find_depth(root.left) + self.find_depth(root.right)
        left_diameter = self.diameterOfBinaryTree(root.left)
        right_diameter = self.diameterOfBinaryTree(root.right)

        return max(current_diameter, left_diameter, right_diameter)