import sys
from typing import List

sys.setrecursionlimit(10 ** 5)


def solution(n: int, inorder: List[int], postorder: List[int]) -> List[int]:
    answer = []

    # inorder 값의 index를 저장
    inorder_index = [0] * (n + 1)
    for i in range(n):
        inorder_index[inorder[i]] = i

    def preorder(in_start, in_end, post_start, post_end):
        # 재귀 종료
        if in_start > in_end or post_start > post_end:
            return

        # 현 트리에서 최상위 루트 (postorder의 마지막)
        root = postorder[post_end]
        answer.append(root)

        # inorder에서의 root 위치 찾기
        in_root = inorder_index[root]

        # 왼쪽 자식트리 노드의 개수
        left_node = in_root - in_start
        preorder(in_start, in_root - 1, post_start, post_start + left_node - 1)

        # 오른쪽 자식트리 노드의 개수
        right_node = in_end - in_root
        preorder(in_root + 1, in_end, post_end - right_node, post_end - 1)

    preorder(0, n - 1, 0, n - 1)

    return answer


n = int(sys.stdin.readline().rstrip())
inorder = list(map(int, sys.stdin.readline().rstrip().split()))
postorder = list(map(int, sys.stdin.readline().rstrip().split()))

print(*solution(n, inorder, postorder))
