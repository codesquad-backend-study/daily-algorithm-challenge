import sys
import collections

n = int(sys.stdin.readline())
graph = collections.defaultdict(list)

for _ in range(n - 1):
    parent, child, weight = map(int, sys.stdin.readline().split())
    graph[parent].append((child, weight))
    graph[child].append((parent, weight))


def find(start_node):
    total = 0
    max_node = 0

    visited = [False] * (n + 1)
    visited[start_node] = True
    queue = collections.deque([(start_node, 0)])

    while queue:
        current_node, weight = queue.popleft()
        if weight > total:
            total = weight
            max_node = current_node
        for next_node, next_weight in graph[current_node]:
            if not visited[next_node]:
                queue.append((next_node, weight + next_weight))
                visited[next_node] = True

    return total, max_node


_, node1 = find(1)
diameter, node2 = find(node1)

print(diameter)
