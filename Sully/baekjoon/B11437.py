import sys
from typing import List

sys.setrecursionlimit(10 ** 5)


def solution(N: int, tree1: List[List[int]], tree2: List[List[int]]) -> List[int]:
    answer = []
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    parent = [i for i in range(N + 1)]
    depth = [0] * (N + 1)

    for t in tree1:
        x, y = t
        graph[x].append(y)
        graph[y].append(x)

    # 방문 여부를 확인하면서
    # 해당 노드(node)와 연결된 노드에 깊이(d)를 1씩 증가시키면서 depth에 기록
    def dfs(node, d):
        visited[node] = True
        depth[node] = d

        for n in graph[node]:
            if not visited[n]:
                parent[n] = node
                dfs(n, d + 1)

    # x, y 노드 중 가장 깊이가 깊은 노드를 y로 통일
    # x, y의 깊이가 같아질 때까지 y를 parent[y]로 업데이트
    # 두 노드의 깊이만큼 부모를 거슬러 올라감
    def lca(x, y):
        if depth[x] > depth[y]:
            y, x = x, y

        while True:
            if depth[x] == depth[y]:
                break

            y = parent[y]

        for _ in range(depth[x]):
            if x == y:
                return x

            x = parent[x]
            y = parent[y]

        return x

    dfs(1, 0)

    for t in tree2:
        x, y = t
        answer.append(lca(x, y))

    return answer


N = int(sys.stdin.readline().rstrip())
array1 = []
for _ in range(N - 1):
    array1.append(list(map(int, sys.stdin.readline().rstrip().split())))

M = int(sys.stdin.readline().rstrip())
array2 = []
for _ in range(M):
    array2.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(*solution(N, array1, array2), sep='\n')
