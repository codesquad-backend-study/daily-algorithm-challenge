import collections

t = int(input())

for _ in range(t):
    n = int(input())
    graph = [[] for _ in range(n + 1)]
    parent = [-1] * (n + 1)
    depth = [-1] * (n + 1)
    parent[0] = 0

    for _ in range(n - 1):
        p, c = map(int, input().split())

        graph[p].append(c)
        parent[c] = p

    root = parent.index(-1)

    queue = collections.deque([(root, 0)])

    while queue:
        node, d = queue.popleft()
        depth[node] = d

        for i in graph[node]:
            queue.append((i, d + 1))


    def find(n1, n2):
        while depth[n1] != depth[n2]:
            if depth[n1] < depth[n2]:
                n2 = parent[n2]
            else:
                n1 = parent[n1]

        while n1 != n2:
            n1 = parent[n1]
            n2 = parent[n2]

        return n1


    n1, n2 = map(int, input().split())
    print(find(n1, n2))
