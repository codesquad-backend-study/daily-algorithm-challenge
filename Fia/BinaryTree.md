## 104번 문제 : 재귀 동작 방식

![leetcode104](https://user-images.githubusercontent.com/105152276/222317255-3c85a69a-4e65-444f-8489-f9522133ea53.jpeg)

## BinaryTree : 탐색 방법들

1. 전위 순회 (Preorder Traversal) : 루트 노드를 먼저 탐색하고 자식 노드를 탐색하는 방식이다.
2. 중위 순회 (Inorder Traversal) : 왼쪽 자식 노드를 탐색하고 루트 노드를 탐색하고 오른쪽 자식 노드를 탐색하는 방식이다.
3. 후위 순회 (Postorder Traversal) : 왼쪽 자식 노드를 탐색하고 오른쪽 자식 노드를 탐색하고 루트 노드를 탐색하는 방식이다.
4. 레벨 순회 (LevelOrder Traversal or BFS, Breath-First Search) : 레벨 순회는 루트 노드를 먼저 탐색하고, 그 다음 레벨의 노드를 탐색하는 방식이다. `Queue`를 하나 선언해두고, 루트 노드를 넣은 다음, `Queue`에서 노드를 하나씩 꺼내 탐색하면서 자식 노드를 `Queue`에 넣는다. `Queue`가 비어있을 때까지 반복한다.

레벨 순회를 제외한 나머지 순회 방식은 DFS, Depth-First Search 깊이 우선 탐색으로 분류할 수 있다.

``` java
public void preOrder(Node root) {
    if (root != null) {
        System.out.println(root.getVal() + " ");
        if (root.left != null) preOrder(root.left);
        if (root.right != null) preOrder(root.right);
    }
}

public void inOrder(Node root) {
    if (root != null) {
        if (root.left != null) inOrder(root.left);
        System.out.println(root.getVal() + " ");
        if (root.right != null) inOrder(root.right);
    }
}

public void postOrder(Node root) {
    if (root != null) {
        if (root.left != null) postOrder(root.left);
        if (root.right != null) postOrder(root.right);
        System.out.println(root.getVal() + " ");
    }
}

public void levelOrder(Node root) {
    Queue<Node> queue = new LinkedList<>();
    queue.offer(root);

    while(!queue.isEmpty()) {
        Node node = queue.poll();
        System.out.print(node.getData() + " ");

        if(node.left != null) queue.offer(node.left);
        if(node.right != null) queue.offer(node.right);
    }
}
```