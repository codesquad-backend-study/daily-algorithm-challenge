import collections
import sys
from typing import List


def solution(N: int, array: List[List[int]]) -> List[int]:
    answer = []
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    parent = [0] * (N + 1)

    for a in array:
        x, y = a
        graph[x].append(y)
        graph[y].append(x)

    def bfs(start):
        dq = collections.deque()
        dq.append(start)
        visited[start] = True

        while dq:
            popped = dq.popleft()

            for p in graph[popped]:
                if not visited[p]:
                    visited[p] = True
                    parent[p] = popped
                    dq.append(p)

    bfs(1)

    for i in parent[2:]:
        answer.append(i)

    return answer


N = int(sys.stdin.readline().rstrip())
array = []
for _ in range(N - 1):
    array.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(*solution(N, array), sep='\n')
