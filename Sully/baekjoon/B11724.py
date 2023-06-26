import sys
from typing import List

sys.setrecursionlimit(10000)


def solution(n: int, nums: List[List[int]]) -> int:
    answer = 0
    graph = [[] * (n + 1) for _ in range(n + 1)]
    visited = [False] * (n + 1)

    for num in nums:
        u, v = num[0], num[1]
        graph[u].append(v)
        graph[v].append(u)

    def dfs(index: int) -> None:
        visited[index] = True

        for i in graph[index]:
            if not visited[i]:
                dfs(i)

    for i in range(1, n + 1):
        if not visited[i]:
            answer += 1
            dfs(i)

    return answer


N, M = map(int, sys.stdin.readline().rstrip().split())
array = []
for _ in range(M):
    array.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(solution(N, array))
