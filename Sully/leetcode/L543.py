# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # root를 지날 수도 있고, 안 지날 수도 있음
    # 거꾸로 올라가야 됨
    def __init__(self):
        self.branch_count = None

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # self를 붙이면 이 클래스의 인스턴스 변수를 생성해준다는 뜻임
        # 그래서 self로 클래스 내에 있는 모든 인스턴스 메서드에서 사용 가능 (여기선 dfs())
        # 결론: self == instance, 자바 인스턴스랑 똑같음 (private 처리 안 된 인스턴스 변수)
        self.branch_count = 0

        # run()
        self.dfs(root)

        return self.branch_count

    def dfs(self, node):
        # node가 null이면 0 리턴
        if node is None:
            return 0

        # 마지막 노드부터 찾고 (재귀 이용)
        left = self.dfs(node.left)
        right = self.dfs(node.right)

        # 이제 거꾸로 올라가야지
        # 노드를 통과하는 가장 긴 나뭇가지 계산 (각각의 left와 right의 경로)
        # left와 right의 자식 노드 거리의 합의 최댓값
        self.branch_count = max(self.branch_count, left + right)
        # 재귀함수 지나갈 때마다 1씩 증가해야 되니
        # 자식 노드 중 큰 값
        return max(left, right) + 1
