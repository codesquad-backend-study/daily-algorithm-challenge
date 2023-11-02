dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def dfs(x, y):
    graph[y][x] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < width and 0 <= ny < height:
            if graph[ny][nx] == 1:
                dfs(nx, ny)


t = int(input())

for _ in range(t):
    width, height, cabbage_cnt = map(int, input().split())

    graph = [[0] * width for _ in range(height)]

    for _ in range(cabbage_cnt):
        x, y = map(int, input().split())
        graph[y][x] = 1

    larva_cnt = 0
    for y in range(height):
        for x in range(width):
            if graph[y][x] == 1:
                larva_cnt += 1
                dfs(x, y)
    print(larva_cnt)
