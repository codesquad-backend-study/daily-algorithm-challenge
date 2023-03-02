def find(depth, node):
    if node is None:
        return depth - 1

    ans = 0
    ans = max(ans, find(depth + 1, node.left))
    ans = max(ans, find(depth + 1, node.right))

    return ans


class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = find(1, root)
        return ans
