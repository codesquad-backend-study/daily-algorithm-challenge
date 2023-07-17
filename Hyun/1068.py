import collections

n = int(input())
parents = list(map(int, input().split()))
remove_node = int(input())

graph = [[] for _ in range(n)]

for idx, parent in enumerate(parents):
    if parent == -1:
        continue
    graph[parent].append(idx)

skip_nodes = {}

queue = collections.deque([(remove_node)])
if parents[remove_node] != -1:
    graph[parents[remove_node]].remove(remove_node)
skip_nodes[remove_node] = 0

while queue:
    node = queue.popleft()

    for i in graph[node]:
        skip_nodes[i] = 0
        queue.append(i)

ans = 0
for idx, child in enumerate(graph):
    if idx not in skip_nodes:
        if len(child) == 0:
            ans += 1

print(ans)
