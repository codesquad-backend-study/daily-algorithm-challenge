from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# inorder: left -> self -> right
# preorder: self -> left -> right
# postorder: left -> right -> self
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        global ret
        ret = []

        self.inorder(root)
        return ret

    def inorder(self, root: Optional[TreeNode]):
        if not root:
            return

        self.inorder(root.left)
        ret.append(root.val)
        self.inorder(root.right)

    # Iterative 스택으로 해보려 했는데 넘 어렵다.. 이건 담에,,
