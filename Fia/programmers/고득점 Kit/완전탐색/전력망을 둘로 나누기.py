import collections


def solution(n, wires):
    gap = 100

    for i in range(len(wires)):
        tower = [[] for _ in range(n + 1)]

        for index, wire in enumerate(wires):
            if index == i: continue

            tower[wire[0]].append(wire[1])
            tower[wire[1]].append(wire[0])

        queue = collections.deque([1])
        visited = [False] * (n + 1)

        while queue:
            current = queue.popleft()
            visited[current] = True

            for node in tower[current]:
                if not visited[node]:
                    queue.append(node)

        gap = min(gap, abs(n - (sum(visited) * 2)))

    return gap
