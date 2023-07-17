for _ in range(int(input())):
    country, n = map(int, input().split())
    graph = [[] for _ in range(country + 1)]

    for _ in range(n):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (country + 1)
    visited[1] = 1

    def dfs(node, count):
        for val in graph[node]:
            if visited[val] == 0:
                visited[val] = 1
                count = dfs(val, count + 1)
        return count

    print(dfs(1, 0))
