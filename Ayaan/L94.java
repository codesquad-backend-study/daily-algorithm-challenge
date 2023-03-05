class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> inorderList = new ArrayList<Integer>();
        return inorder(root, inorderList);
    }

    public List<Integer> inorder(TreeNode node, List<Integer> inorderList){
        if(node == null){
            return inorderList;
        }

        TreeNode left = node.left;

        if(left != null){
            inorder(left, inorderList);
        }

        inorderList.add(node.val);

        TreeNode right = node.right;

        if(right != null){
            inorder(right, inorderList);
        }

        return inorderList;
    }
}