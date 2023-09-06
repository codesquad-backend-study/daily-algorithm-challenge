import collections
import sys
from typing import List


def solution(N: int, tree: List[List[int]], A: int, B: int) -> int:
    # A부터 부모 노드까지의 경로 지정 후
    # B부터 부모 노트까지 탐색하며 A 경로와 겹치는 노드를 찾으면 됨

    graph = collections.defaultdict(list)

    for t in tree:
        a, b = t
        graph[b] = a

    # A의 부모 노드들 배열 생성
    A_parent = []
    while A in graph:
        A_parent.append(A)
        A = graph[A]

    # B의 부모 노드로 올라가면서
    # A의 부모 노드 배열에 있는지 확인
    while B in graph:
        if B in A_parent:
            break

        B = graph[B]

    return B


T = int(sys.stdin.readline().rstrip())
for _ in range(T):
    N = int(sys.stdin.readline().rstrip())
    tree = []
    for _ in range(N - 1):
        A_B = list(map(int, sys.stdin.readline().rstrip().split()))
        tree.append(A_B)

    A, B = map(int, sys.stdin.readline().rstrip().split())

    print(solution(N, tree, A, B))
