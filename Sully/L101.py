# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    # stack 방법 -> 파이선 문법 땜에 헤맴..
    # 21ms, 61.63%
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 루트가 없으면 아무것도 존재하지 않으니 사실상 대칭임 -> 참
        if root is None:
            return True

        # list 형태의 stack에 left, right 푸시
        stack = [root.left, root.right]

        # stack이 빌 때까지 계속 반복
        while stack:  # is not None <- 이게 문제
            left_node = stack.pop()
            right_node = stack.pop()

            # 둘 다 null이면 자식을 저장할 필요 X
            if left_node is None and right_node is None:
                continue

            # null 값의 대칭 판단
            if left_node is None or right_node is None:
                return False
            # 아래처럼 할 필요 없이 or 문법이 경우 다 처리해줌
            # if (left_node.val is None and right_node.val is not None) or (
            #         left_node.val is not None and right_node.val is None):
            #     return False

            # 단순 변수 비교
            if left_node.val != right_node.val:
                return False

            stack.append(left_node.left)
            stack.append(right_node.right)
            stack.append(left_node.right)
            stack.append(right_node.left)

        return True

    # 재귀 방법
    # 24ms, 35.79%
    def isSymmetric(self, root):
        if root is None:
            return True

        return self.check_node(root.left, root.right)

    def check_node(self, left_node, right_node):
        if left_node is None and right_node is None:
            return True

        if left_node is None or right_node is None:
            return False

        if left_node.val != right_node.val:
            return False

        return self.check_node(left_node.left, right_node.right) and self.check_node(left_node.right, right_node.left)
