def solution():
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [False] * (N + 1)
    def dfs(node):
        visited[node] = True

        for num in graph[node]:
            if not visited[num]:
                dfs(num)

    result = 0
    for i in range(1, N + 1):
        if not visited[i]:
            result += 1
            dfs(i)
    print(result)

solution()
