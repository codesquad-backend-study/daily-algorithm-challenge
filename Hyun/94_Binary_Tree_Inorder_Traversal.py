def inorder(node, ans: list):
    if node is None:
        return

    inorder(node.left, ans)
    ans.append(node.val)
    inorder(node.right, ans)                        # 재귀함수 사용


class Solution1:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        inorder(root, ans)
        return ans


## Follow up: Recursive solution is trivial, could you do it iteratively? ##
# 못하겠음 ㅋ

