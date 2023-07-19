import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

# 중위 순회의 각 값의 위치 값 저장
in_position = [0] * (n + 1)
for i in range(n):
    in_position[inorder[i]] = i

def preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return

    # 후위 순회의 마지막 값이 루트
    root = postorder[post_end]
    print(root, end=' ')

    # 중위 순회에서 root의 위치를 기준으로 왼쪽 / 오른쪽 서브 트리의 노드 개수를 구한다.
    left_cnt = in_position[root] - in_start
    right_cnt = in_end - in_position[root]

    # 중위 순회와 후위 순회를 왼쪽/오른쪽 서브 트리로 나누고
    # 왼쪽, 오른쪽을 차례대로 재귀를 돈다.(전위 순회 방식에 맞게)
    # preorder(중위 순회의 왼쪽 서브 트리, 후위 순회의 왼쪽 서브 트리)
    preorder(in_start, in_start + left_cnt - 1, post_start, post_start + left_cnt - 1)
    # preorder(중위 순회의 오른쪽 서브 트리, 후위 순회의 오른쪽 서브 트리)
    preorder(in_end - right_cnt + 1, in_end, post_end - right_cnt, post_end - 1)

preorder(0, n-1, 0, n-1)
