package Fia.leetcode;

import java.util.ArrayDeque;
import java.util.Deque;

public class Fia101 {
    Deque<TreeNode> left = new ArrayDeque<>();
    Deque<TreeNode> right = new ArrayDeque<>();

    public boolean isSymmetric(TreeNode root) {
        if (root.left == null && root.right == null) {
            return true;
        }

        if (root.left == null || root.right == null) {
            return false;
        }

        left.add(root.left);
        right.add(root.right);

        while (!left.isEmpty() && !right.isEmpty()) {
            TreeNode leftNode = left.poll();
            if (leftNode.left != null) left.add(leftNode.left);

            TreeNode rightNode = right.poll();
            if (rightNode.right != null) right.add(rightNode.right);

            if (left.peekLast() == null && right.peekLast() != null) return false;

            if (left.peekLast() != null && right.peekLast() == null) return false;

            if (left.peekLast() != null && right.peekLast() != null && left.peekLast().val != right.peekLast().val) return false;

            if (leftNode.right != null) left.add(leftNode.right);
            if (rightNode.left != null) right.add(rightNode.left);

            if (leftNode.val != rightNode.val) return false;

        }
        return true;
    }
}
