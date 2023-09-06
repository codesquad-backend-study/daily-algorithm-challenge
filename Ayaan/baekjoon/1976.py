import collections
import sys
sys.setrecursionlimit(10**9)

N = int(input())
graph = collections.defaultdict(list)
# 양방향 그래프로 만든다.
for _ in range(N - 1):
    node1, node2, weight = map(int, input().split())
    graph[node1].append((node2, weight))
    graph[node2].append((node1, weight))

def dfs(root, weight):
    for node in graph[root]:
        num, node_weight = node
        if visited[num] == -1:
            visited[num] = node_weight + weight
            dfs(num, node_weight + weight)

# 1번 노드에서 제일 먼 거리 노드 구하기
visited = [-1] * (N + 1)
visited[1] = 0
dfs(1, 0)
first_long_node = visited.index(max(visited))
# 그 다음 거기서 제일 먼 노드와의 거리 구하기
visited = [-1] * (N + 1)
visited[first_long_node] = 0
dfs(first_long_node, 0)
print(max(visited))
