import sys
from typing import List


def solution(n: int, nums: List[List[int]]) -> int:
    # "주어지는 비행 스케줄은 항상 연결 그래프를 이룬다." -> 모든 국가가 비행기로 연결되어 있다는 것
    # 즉, 최소 신장 트리의 간선의 개수를 구하는 문제

    # 최소 신장 트리의 간선의 개수: (노드의 개수) - 1
    # 이 문제에서 노드는 국가이므로 -> (국가의 개수) - 1이 정답

    # MST: https://jeonyeohun.tistory.com/93

    return n - 1


T = int(sys.stdin.readline().rstrip())
array = []
for _ in range(T):
    N, M = map(int, sys.stdin.readline().rstrip().split())
    for _ in range(M):
        array.append(list(map(int, sys.stdin.readline().rstrip().split())))

    print(solution(N, array))
