from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    for a, b in tickets:
        graph[a].append(b)

    visited = {}
    ticket_count = 1
    for airport in graph:
        visited[airport] = [False] * len(graph[airport])
        ticket_count += len(graph[airport])

    answer = []

    def travel(current_airport, path):
        next_airports = sorted(graph[current_airport])

        if len(path) == ticket_count:
            answer.extend(path)
            return

        for i, na in enumerate(next_airports):
            if len(answer) > 0:
                return

            if not visited[current_airport][i]:
                visited[current_airport][i] = True
                travel(na, path + [na])
                visited[current_airport][i] = False

    travel('ICN', ['ICN'])

    return answer
