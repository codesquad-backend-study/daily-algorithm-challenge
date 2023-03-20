package Fia;

public class Fia543 { // 최적화 정답
    int answer = 0; // 멤버 변수를 추가하여 최대 깊이를 구함과 동시에 계속하여 가장 긴 루트를 구하는 것이 매우 빠르다.

    public int diameterOfBinaryTree(TreeNode root) {
        maxDepth(root);
        return answer;
    }

    public int maxDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int left = maxDepth(root.left);
        int right = maxDepth(root.right);

        answer = Math.max(answer, left + right); // 최대 깊이를 구하는 메서드와 가장 루트를 구하는 메서드를 하나로 만들어 노드의 수만큼 계산을 수행한다. O(n) : n = 노드의 개수

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
