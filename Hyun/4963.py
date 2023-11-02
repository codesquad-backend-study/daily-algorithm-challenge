def dfs(x, y):
    graph[y][x] = 0

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h:
            if graph[ny][nx] == 1:
                dfs(nx, ny)


dx = [1, 1, 0, -1, -1, -1, 0, 1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

while True:
    w, h = map(int, input().split())

    if w == h == 0:
        break

    graph = [list(map(int, input().split())) for _ in range(h)]

    count = 0
    for y in range(h):
        for x in range(w):
            if graph[y][x] == 1:
                count += 1
                dfs(x, y)

    print(count)
