# 트리 지름 증명: https://blog.myungwoo.kr/112
import collections
import sys
from typing import List


def solution(n: int, array: List[List[int]]) -> int:
    graph = [[] for _ in range(n + 1)]

    for a in array:
        x, y, z = a
        graph[x].append([y, z])
        graph[y].append([x, z])

    def bfs(start):
        visited = [-1 for _ in range(n + 1)]
        visited[start] = 0

        dq = collections.deque()
        dq.append([start, 0])

        maximum = [0, 0]

        while dq:
            current, way = dq.popleft()

            for next, distance in graph[current]:
                if visited[next] == -1:
                    visited[next] = way + distance
                    dq.append([next, visited[next]])

                    if maximum[1] < visited[next]:
                        maximum = [next, visited[next]]

        return maximum

    node, distance = bfs(1)
    node, distance = bfs(node)

    return distance


n = int(sys.stdin.readline().rstrip())
array = []
for _ in range(n - 1):
    array.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(solution(n, array))
