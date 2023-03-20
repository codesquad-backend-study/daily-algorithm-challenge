import collections


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        left_values = []
        right_values = []

        if root.left is not None:
            left_values = self.left_level_order_traverse(root.left)

        if root.right is not None:
            right_values = self.right_level_order_traverse(root.right)

        if len(left_values) != len(right_values):
            return False

        for i in range(len(left_values)):
            if left_values[i] != right_values[i]:
                return False

        return True

    def left_level_order_traverse(self, node):
        values = []

        queue = collections.deque()

        queue.append((node, '0'))

        while queue:
            current_node, sequence = queue.popleft()
            values.append((current_node.val, sequence))

            if current_node.left is not None:
                queue.append((current_node.left, sequence + '1'))

            if current_node.right is not None:
                queue.append((current_node.right, sequence + '2'))

        return values

    def right_level_order_traverse(self, node):
        values = []

        queue = collections.deque()

        queue.append((node, '0'))

        while queue:
            current_node, sequence = queue.popleft()
            values.append((current_node.val, sequence))

            if current_node.right is not None:
                queue.append((current_node.right, sequence + '1'))

            if current_node.left is not None:
                queue.append((current_node.left, sequence + '2'))

        return values