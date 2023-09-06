# 바이러스
def dfs(computer):
    visited[computer] = True

    for node in graph[computer]:
        if not visited[node]:
            dfs(node)


nodes = int(input())
graph = {i: [] for i in range(1, nodes + 1)}
visited = [False] * (nodes + 1)

line = int(input())
for _ in range(line):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

dfs(1)
print(sum(visited) - 1)
