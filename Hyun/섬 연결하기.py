import heapq


def solution(n, costs):
    graph = [[] for _ in range(n)]

    for cost in costs:
        n1 = cost[0]
        n2 = cost[1]

        graph[n1].append((n2, cost[2]))
        graph[n2].append((n1, cost[2]))

    d = [-1] * n

    heap = []
    heapq.heappush(heap, (0, 0))

    while heap:
        cost, node = heapq.heappop(heap)

        if d[node] != -1:
            continue

        d[node] = cost

        for node, c in graph[node]:
            heapq.heappush(heap, (c, node))

    return sum(d)
