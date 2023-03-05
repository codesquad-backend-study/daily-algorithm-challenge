# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 중위순회 : 왼쪽노드 -> 현재노드 -> 오른쪽노드
# 스택에 현재노드 저장 후 왼쪽노드 전부 탐색.
# 왼쪽노드에 더 이상 노드가 존재하지 않을 때, 스택에서 현재 노드를 꺼내고 result에 저장 후 오른쪽 노드를 기준으로 다시 탐색 시작.

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        node = root
    
        while stack or node: # 노드 null이고 stack이 비어있으면 종료.
            if node:
                stack.append(node)
                node = node.left # 왼쪽 먼저 탐색
            else: # node가 null일 때
                node = stack.pop()
                result.append(node.val)
                node = node.right
    
        return result
