# 연결 요소의 개수
import sys


def dfs(node):
    visited[node] = True
    for other_node in graph[node]:
        if not visited[other_node]:
            dfs(other_node)


nodes, edges = map(int, input().split())

graph = {vertex: [] for vertex in range(1, nodes + 1)}
visited = [False] * (nodes + 1)

for _ in range(edges):
    node1, node2 = map(int, sys.stdin.readline().strip().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

count = 0

for i in range(1, nodes + 1):
    if not visited[i]:
        dfs(i)
        count += 1

print(count)
