package Fia.leetcode;

public class Fia104 { // LeetCode 226번 문제 solution 참고
    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = maxDepth(root.left);
        int right = maxDepth(root.right);

        return Math.max(left, right) + 1;
    }
}

// python code

// class Solution:
//     def maxDepth(self, root: Optional[TreeNode]) -> int:
//     if not root:
//         return 0
//     left = self.maxDepth(root.left)
//     right = self.maxDepth(root.right)
//     return max(left, right) + 1

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
