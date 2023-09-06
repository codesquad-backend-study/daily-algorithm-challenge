# DFS와 BFS
import collections


def dfs(graph, start_node):
    visited[start_node] = True
    print(start_node, end=" ")

    for node in graph[start_node]:
        if not visited[node]:
            dfs(graph, node)


def bfs(graph, start_node):
    queue = collections.deque([start_node])
    visited[start_node] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")

        for vertex in graph[node]:
            if not visited[vertex]:
                queue.append(vertex)
                visited[vertex] = True


# 문제 풀이
node, edge, start_node = map(int, input().split())

graph = [[] for _ in range(node + 1)]

for _ in range(edge):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for graph_list in graph:
    graph_list.sort()

visited = [False] * (node + 1)
dfs(graph, start_node)

print()

visited = [False] * (node + 1)
bfs(graph, start_node)
