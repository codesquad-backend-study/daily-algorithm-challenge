# 섬의 개수
nx = [0, 0, 1, 1, 1, -1, -1, -1]
ny = [1, -1, 0, 1, -1, 0, 1, -1]


def dfs(row, column):
    graph[row][column] = "0"

    for i in range(8):
        r, c = row + nx[i], column + ny[i]
        if 0 <= r < len(graph) and 0 <= c < len(graph[r]):
            if graph[r][c] == "1":
                dfs(r, c)


string = input()
while string != "0 0":
    island = 0
    width, height = map(int, string.split())
    graph = [input().split() for _ in range(height)]

    for i in range(height):
        for j in range(width):
            if graph[i][j] == "1":
                dfs(i, j)
                island += 1
    print(island)
    string = input()


