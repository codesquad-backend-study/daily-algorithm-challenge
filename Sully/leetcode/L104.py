# 이진 트리 루트가 주어지면 -> 그 최대 깊이 리턴
# 이진 트리의 최대 깊이 -> 루트 노드에서 가장 먼 리프 노드까지 가장 긴 경로의 노드 수

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 재귀(아래에서 위로) -> 최대 깊이: 좌측 자식 트리와, 우측 자식 트리 중 큰 값
        if not root:
            return 0

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1

        # 스택(위에서 아래로) -> 경우에 따라 더 복잡쓰
        # if not root:
        #     return 0
        #
        # max_depth = 0
        # stack = [(root, 1)]
        # while stack:
        #     node, depth = stack.pop()
        #     max_depth = max(depth, max_depth)
        #     if node.left:
        #         stack.append((node.left, depth + 1))
        #     if node.right:
        #         stack.append((node.right, depth + 1,))
        #
        # return max_depth
