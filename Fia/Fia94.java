package Fia;

import java.util.ArrayList;
import java.util.List;

public class Fia94 {
    List<Integer> answer = new ArrayList<>();
    public List<Integer> inorderTraversal(TreeNode root) {
        if (root == null) return answer;
        if (root.left != null) {
            inorderTraversal(root.left);
        }
        answer.add(root.val);
        if (root.right != null) {
            inorderTraversal(root.right);
        }
        return answer;
    }
}
