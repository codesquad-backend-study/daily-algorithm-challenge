# LCA
import collections
import sys

number_of_node = int(sys.stdin.readline())

trees = collections.defaultdict(list)
for _ in range(number_of_node - 1):
    node1, node2 = map(int, sys.stdin.readline().split())
    trees[node1].append(node2)
    trees[node2].append(node1)

number_of_tuple = int(sys.stdin.readline())

tuples = []
for _ in range(number_of_tuple):
    node1, node2 = map(int, sys.stdin.readline().split())
    tuples.append((node1, node2))

depths = [0] * (number_of_node + 1)
parents = [0] * (number_of_node + 1)

visited = set()
queue = collections.deque([1])

while queue:
    node = queue.popleft()
    visited.add(node)

    for child in trees[node]:
        if child not in visited:
            depths[child] = depths[node] + 1
            parents[child] = node
            queue.append(child)


def LCA(a, b):
    if depths[a] < depths[b]:  # 더 깊이 있는 node가 a가 된다
        a, b = b, a
    gap = depths[a] - depths[b]  # 차이만큼 더 깊이 있는 node만 부모를 타고 올라가고
    for _ in range(gap):
        a = parents[a]
    while a != b:  # 부모가 같아질 때까지 두 노드 모두 부모를 타고 올라간다
        a = parents[a]
        b = parents[b]
    return a


for node1, node2 in tuples:
    print(LCA(node1, node2))
