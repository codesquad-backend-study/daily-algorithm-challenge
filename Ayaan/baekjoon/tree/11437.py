import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

depths = [0] * (n + 1)
parent = [0] * (n + 1)
visited = [False] * (n + 1)

# 각 노드의 깊이와 부모 노드를 구한다.
def dfs(root, depth):
    visited[root] = True
    depths[root] = depth

    for child in graph[root]:
        if not visited[child]:
            parent[child] = root
            dfs(child, depth + 1)

def lca(a, b):
    # 깊이가 같아질 때까지 부모로 이동
    while depths[a] != depths[b]:
        if depths[a] > depths[b]:
            a = parent[a]
        else:
            b = parent[b]

    # 공통 조상이 나올 때까지 부모로 이동
    while a != b:
        a = parent[a]
        b = parent[b]

    return a

dfs(1, 0)

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(lca(a, b))
