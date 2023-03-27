package Ayaan;

public class L104 {
    public static void main(String[] args) {
        TreeNode node1 = new TreeNode(15);
        TreeNode node2 = new TreeNode(7);
        TreeNode node3 = new TreeNode(20, node1, node2);

        TreeNode node4 = new TreeNode(9);
        TreeNode root = new TreeNode(3, node3, node4);

        int result = maxDepth(root);
        System.out.println(result);
    }

    public static int maxDepth(TreeNode root){
        if(root == null){
            return 0;
        }

        int left_depth = maxDepth(root.left);
        int right_depth = maxDepth(root.right);

        return Math.max(left_depth, right_depth) + 1;
    }
}
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