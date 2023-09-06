# 안전 영역

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
max_height = max(max(row) for row in graph)

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(row, column):
    visited[row][column] = True

    for k in range(4):
        next_row, next_column = row + dx[k], column + dy[k]
        if 0 <= next_row < N and 0 <= next_column < N:
            if not visited[next_row][next_column] and graph[next_row][next_column] >= height:
                dfs(next_row, next_column)


answer = []
for height in range(1, max_height + 1):
    count = 0
    visited = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visited[i][j] and graph[i][j] >= height:
                dfs(i, j)
                count += 1
    answer.append(count)

print(max(answer))
