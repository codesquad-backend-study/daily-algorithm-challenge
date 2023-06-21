from collections import deque

def dfs_and_bfs():
    N, M, V = map(int, input().split())

    graph = [[False] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        start, end = map(int, input().split())
        graph[start][end] = True
        graph[end][start] = True

    dfs_visited = [False] * (N + 1)
    bfs_visited = [False] * (N + 1)

    def dfs(node):
        print(node, end=" ")
        dfs_visited[node] = True

        for i in range(1, N + 1):
            if dfs_visited[i]:
                continue
            if graph[node][i]:
                dfs(i)

    def bfs(node):
        q = deque([node])
        bfs_visited[node] = True
        while q:
            node = q.popleft()
            print(node, end=" ")
            for i in range(1, N + 1):
                if bfs_visited[i]:
                    continue
                if graph[node][i]:
                    q.append(i)
                    bfs_visited[i] = True

    dfs(V)
    print()
    bfs(V)

dfs_and_bfs()
