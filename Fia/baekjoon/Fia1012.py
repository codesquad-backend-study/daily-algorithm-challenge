# 유기농 배추
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(r, c):
    cabbages[r][c] = 0

    for i in range(4):
        nx = c + dx[i]
        ny = r + dy[i]
        if 0 <= nx < column and 0 <= ny < row:
            if cabbages[ny][nx] == 1:
                dfs(ny, nx)


T = int(input())

for _ in range(T):
    column, row, count = map(int, input().split())
    cabbages = [[0] * column for _ in range(row)] # map이 아닌 list 사용 시 통과

    for _ in range(count):
        x, y = map(int, input().split())
        cabbages[y][x] = 1

    count = 0
    for i in range(row):
        for j in range(column):
            if cabbages[i][j] == 1:
                dfs(i, j)
                count += 1

    print(count)
