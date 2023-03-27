class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root, inorderList):
            if not root:
                return root
            
            if root.left:
                inorder(root.left, inorderList)
            inorderList.append(root.val)
            if root.right:
                inorder(root.right, inorderList)
            return inorderList

        inorderList = []
        return inorder(root, inorderList)