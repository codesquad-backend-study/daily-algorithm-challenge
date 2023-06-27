def solution():
    n = int(input())
    graph = []
    max_num = 0

    for _ in range(n):
        input_data = list(map(int, input().split()))
        graph.append(input_data)
        max_num = max(max_num, max(input_data))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    def dfs(x, y, height):
        visited[x][y] = True

        for i in range(4):
            mx = x + dx[i]
            my = y + dy[i]
            if 0 <= mx < n and 0 <= my < n and \
                    not visited[mx][my] and graph[mx][my] > height:
                dfs(mx, my, height)


    max_count = 1
    for height in range(1, max_num):
        visited = [[False] * n for _ in range(n)]
        count = 0
        for i in range(n):
            for j in range(n):
                if not visited[i][j] and graph[i][j] > height:
                    count += 1
                    dfs(i, j, height)
        max_count = max(max_count, count)
    print(max_count)

solution()
