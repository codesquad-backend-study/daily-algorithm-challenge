import sys
from typing import List


def solution(N: int, tree: List[int], remove: int):
    answer = 0

    def dfs(remove_node):
        # 나중 판별을 위한 무시해도 되는 숫자 (어차피 제거됨)
        tree[remove_node] = -999

        for i in range(N):
            # remove_node의 자식이 tree[i]라면
            if remove_node == tree[i]:
                dfs(i)

    dfs(remove)

    for i in range(N):
        # 아까 설정한 무시해도 되는 제거된 노드가 아닐 때
        # and
        # i의 자식이 없을 때
        if tree[i] != -999 and i not in tree:
            answer += 1

    return answer


N = int(sys.stdin.readline().rstrip())
tree = list(map(int, sys.stdin.readline().rstrip().split()))
remove = int(sys.stdin.readline().rstrip())

print(solution(N, tree, remove))
