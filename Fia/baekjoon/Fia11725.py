import sys
import collections

N = int(sys.stdin.readline())
trees = collections.defaultdict(list)

for _ in range(N - 1):
    node1, node2 = map(int, sys.stdin.readline().split())
    trees[node1].append(node2)
    trees[node2].append(node1)

parents = [0] * (N + 1)

# dfs 풀이   440ms
# visited = set()
#
#
# def traversal(root):
#     visited.add(root)
#     for node in trees[root]:
#         if parents[node] == 0:
#             parents[node] = root
#     for node in trees[root]:
#         if node not in visited:
#             traversal(node)
#
#
# traversal(1)

# bfs 풀이   356ms
queue = collections.deque([1])
while queue:
    parent = queue.popleft()
    for node in trees[parent]:
        if parents[node] == 0:
            parents[node] = parent
            queue.append(node)

print(*parents[2:], sep='\n')
