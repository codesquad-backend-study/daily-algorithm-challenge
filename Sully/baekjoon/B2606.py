import sys
from typing import List


def solution(n: int, computers: List[List[int]]) -> int:
    global answer

    answer = 0
    visited = [False] * (n + 1)
    graph = [[] * (n + 1) for _ in range(n + 1)]

    for computer in computers:
        x, y = computer[0], computer[1]
        graph[x].append(y)
        graph[y].append(x)

    def dfs(index: int) -> None:
        global answer

        visited[index] = True

        for i in graph[index]:
            if not visited[i]:
                answer += 1
                dfs(i)

    dfs(1)

    return answer


N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
array = []
for _ in range(M):
    array.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(solution(N, array))
