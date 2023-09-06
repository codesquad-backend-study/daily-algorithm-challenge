import collections
import sys
from typing import List


def solution(array: List[List[str]]) -> List[List[str]]:
    answer = []
    tree = collections.defaultdict(list)

    for c in array:
        root, left, right = c
        tree[root] = [left, right]

    # 전위: root -> left -> right
    def preorder(node):
        if node == '.':
            return

        tmp.append(node)
        preorder(tree[node][0])
        preorder(tree[node][1])

    # 중위: left -> root -> right
    def inorder(node):
        if node == '.':
            return

        inorder(tree[node][0])
        tmp.append(node)
        inorder(tree[node][1])

    # gn위: left -> right -> root
    def postorder(node):
        if node == '.':
            return

        postorder(tree[node][0])
        postorder(tree[node][1])
        tmp.append(node)

    tmp = []
    preorder('A')
    answer.append(tmp)

    tmp = []
    inorder('A')
    answer.append(tmp)

    tmp = []
    postorder('A')
    answer.append(tmp)

    return answer


N = int(sys.stdin.readline().rstrip())
array = []
for _ in range(N):
    array.append(list(sys.stdin.readline().rstrip().split()))

result = solution(array)
for x in result:
    print(''.join(x))
