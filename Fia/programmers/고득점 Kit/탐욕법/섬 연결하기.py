from heapq import heappush
from heapq import heappop


def solution(n, costs):
    graph = [[] for _ in range(n)]

    for a, b, cost in costs:
        graph[a].append((cost, b))
        graph[b].append((cost, a))

    index = 0
    visited = [False] * n

    while not graph[index]:
        index += 1

    visited[index] = True
    heap = []

    for node in graph[index]:
        heappush(heap, node)

    total = 0

    while heap:
        weight, node = heappop(heap)

        if visited[node]:
            continue

        total += weight
        visited[node] = True

        for child in graph[node]:
            if not visited[child[1]]:
                heappush(heap, child)

    return total
