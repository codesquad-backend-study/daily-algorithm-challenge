package Fia;

import java.util.LinkedList;
import java.util.Queue;

public class Fia543 {
    public int diameterOfBinaryTree(TreeNode root) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root);

        int answer = 0;
        while (!queue.isEmpty()) {
            TreeNode node = queue.poll();
            answer = Math.max(answer, maxDiameter(node));

            if(node.left != null) queue.offer(node.left);
            if(node.right != null) queue.offer(node.right);
        }
        return answer;
    }

    public int maxDiameter(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = maxDepth(root.left);
        int right = maxDepth(root.right);

        return left + right;
    }

    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = maxDepth(root.left);
        int right = maxDepth(root.right);

        return Math.max(left, right) + 1;
    }
}

class TreeNodeTwo {
     int val;
     TreeNode left;
     TreeNode right;
     TreeNodeTwo() {}
     TreeNodeTwo(int val) { this.val = val; }
     TreeNodeTwo(int val, TreeNode left, TreeNode right) {
         this.val = val;
         this.left = left;
         this.right = right;
     }
 }
