# 트리의 순회
import sys

n = int(sys.stdin.readline().strip())
inorder = list(map(int, sys.stdin.readline().strip().split()))
postorder = list(map(int, sys.stdin.readline().strip().split()))

inorder_index = [0] * (n + 1)
for i in range(n):
    inorder_index[inorder[i]] = i


def preorder(inorder_start, inorder_end, post_start, post_end):
    if (inorder_start > inorder_end) or (post_start > post_end):
        return

    root = postorder[post_end]

    left = inorder_index[root] - inorder_start
    right = inorder_end - inorder_index[root]

    print(root, end=" ")
    preorder(inorder_start, inorder_start + left - 1, post_start, post_start + left - 1)
    preorder(inorder_end - right + 1, inorder_end, post_end - right, post_end - 1)


preorder(0, n - 1, 0, n - 1)
