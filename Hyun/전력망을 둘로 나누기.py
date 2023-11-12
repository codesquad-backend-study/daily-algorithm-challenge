def solution(n, wires):
    graph = [[] for _ in range(n + 1)]

    for n1, n2 in wires:
        graph[n1].append(n2)
        graph[n2].append(n1)

    def dfs(node):
        visit = [False] * (n + 1)

        def go(n):
            visit[n] = True
            count = 1
            for i in graph[n]:
                if not visit[i]:
                    count += go(i)
            return count

        return go(node)

    ans = 100000

    for n1, n2 in wires:
        graph[n1].remove(n2)
        graph[n2].remove(n1)

        ans = min(ans, abs(dfs(n1) - dfs(n2)))

        graph[n1].append(n2)
        graph[n2].append(n1)

    return ans
