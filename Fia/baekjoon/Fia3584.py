# 가장 가까운 공통 조상
import collections
import sys


def solution():
    number_of_node = int(sys.stdin.readline())
    parents = [0] * (number_of_node + 1)
    trees = collections.defaultdict(list)
    for _ in range(number_of_node - 1):
        parent, child = map(int, sys.stdin.readline().split())
        parents[child] = parent
        trees[parent].append(child)

    root = parents[1:].index(0) + 1
    depths = [0] * (number_of_node + 1)
    queue = collections.deque([root])

    while queue:
        parent = queue.popleft()
        for child in trees[parent]:
            depths[child] = depths[parent] + 1
            if len(trees[child]) > 0:
                queue.append(child)

    def LCA(a, b):
        if depths[a] < depths[b]:
            a, b = b, a
        gap = depths[a] - depths[b]
        for _ in range(gap):
            a = parents[a]
        while a != b:
            a = parents[a]
            b = parents[b]
        return a

    node1, node2 = map(int, sys.stdin.readline().split())
    print(LCA(node1, node2))


test_case = int(sys.stdin.readline())
for _ in range(test_case):
    solution()
