import collections
import sys
from typing import List


def solution(n: int, v: int, nums: List[List[int]]) -> List[List[int]]:
    dfs_answer, bfs_answer = [], []
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    dfs_visited = [False] * (n + 1)
    bfs_visited = [False] * (n + 1)

    for num in nums:
        x, y = num[0], num[1]
        graph[x][y] = 1
        graph[y][x] = 1

    def dfs(dfs_v) -> None:
        dfs_visited[dfs_v] = True
        dfs_answer.append(dfs_v)

        for i in range(1, n + 1):
            if not dfs_visited[i] and graph[dfs_v][i] == 1:
                dfs(i)

    def bfs(bfs_v) -> None:
        bfs_visited[bfs_v] = True
        dq = collections.deque()
        dq.append(bfs_v)

        while dq:
            popped = dq.popleft()
            bfs_answer.append(popped)

            for i in range(1, n + 1):
                if not bfs_visited[i] and graph[popped][i] == 1:
                    dq.append(i)
                    bfs_visited[i] = True

    dfs(v)
    bfs(v)

    return [dfs_answer, bfs_answer]


N, M, V = map(int, sys.stdin.readline().rstrip().split())
array = []
for _ in range(M):
    array.append(list(map(int, sys.stdin.readline().rstrip().split())))

for x in solution(N, V, array):
    print(' '.join(map(str, x)))
