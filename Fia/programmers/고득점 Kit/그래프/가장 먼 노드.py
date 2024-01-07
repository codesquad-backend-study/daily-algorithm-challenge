import collections


def solution(n, edge):
    visited = [60000] * (n + 1)
    graph = collections.defaultdict(set)

    for a, b in edge:
        graph[a].add(b)
        graph[b].add(a)

    queue = collections.deque([(1, 0)])
    visited[1] = 0
    max_distance = 0

    while queue:
        node, distance = queue.popleft()

        for child in graph[node]:
            if visited[child] > distance + 1:
                visited[child] = distance + 1
                queue.append((child, distance + 1))
                max_distance = max(max_distance, distance + 1)

    return visited.count(max_distance)
