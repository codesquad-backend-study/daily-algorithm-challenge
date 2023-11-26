from collections import deque


def solution(n, computers):
    visited = [False] * n
    graph = [[] for _ in range(n)]

    for idx, computer in enumerate(computers):
        for i, connect in enumerate(computer):
            if i == idx: continue

            if connect == 1:
                graph[idx].append(i)
                graph[i].append(idx)

    answer = 0

    for node in range(n):

        if not visited[node]:
            queue = deque([node])
            visited[node] = True

            while queue:
                current = queue.popleft()

                for child in graph[current]:
                    if not visited[child]:
                        queue.append(child)
                        visited[child] = True
            answer += 1

    return answer
