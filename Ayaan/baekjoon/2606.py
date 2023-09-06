def virus():
    N = int(input())
    network = [[] for _ in range(N + 1)]
    for _ in range(int(input())):
        a, b = map(int, input().split())
        network[a].append(b)
        network[b].append(a)

    visited = [False] * (N + 1)
    result = []
    def dfs(node):
        result.append(node)
        visited[node] = True

        for com in network[node]:
            if not visited[com]:
                dfs(com)

    dfs(1)
    print(len(result) - 1)

virus()
