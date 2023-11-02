import sys

sys.setrecursionlimit(10 ** 5)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

preorder = []

sub_cnt = {val: idx for idx, val in enumerate(inorder)}


def split(inorder_start, inorder_end, postorder_start, postorder_end):
    if postorder_end - postorder_start <= 0:
        return

    root = postorder[postorder_end - 1]
    preorder.append(root)

    if postorder_end - postorder_start <= 1:
        return

    left_node_cnt = sub_cnt[root] - inorder_start
    right_node_cnt = inorder_end - sub_cnt[root] - 1

    split(inorder_start, inorder_start + left_node_cnt, postorder_start, postorder_start + left_node_cnt)
    split(inorder_end - right_node_cnt, inorder_end, postorder_end - right_node_cnt - 1, postorder_end - 1)


split(0, len(inorder), 0, len(postorder))

print(*preorder)
