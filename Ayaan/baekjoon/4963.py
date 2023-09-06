def solution():
    def island(width, height):
        graph = []
        for _ in range(height):
            graph.append(list(map(int, input().split())))

        dx = [-1, -1, 0, 1, 1, 1, 0, -1]
        dy = [0, 1, 1, 1, 0, -1, -1, -1]

        def dfs(x, y):
            graph[x][y] = 0

            for i in range(8):
                move_x = x + dx[i]
                move_y = y + dy[i]
                if 0 <= move_x < height and 0 <= move_y < width and graph[move_x][move_y] == 1:
                    dfs(move_x, move_y)

        count = 0
        for i in range(height):
            for j in range(width):
                if graph[i][j] == 1:
                    count += 1
                    dfs(i, j)
        print(count)

    while True:
        width, height = map(int, input().split())
        if width == 0 and height == 0:
            return
        island(width, height)

solution()
