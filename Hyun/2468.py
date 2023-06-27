import sys

sys.setrecursionlimit(10 ** 6)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]
max_height = max(map(max, graph))


def dfs(x, y):
    graph[y][x] -= 1
    visit[y][x] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visit[ny][nx] and graph[ny][nx] > 0:
                dfs(nx, ny)


max_cnt = 1
for _ in range(max_height + 1):
    visit = [[False] * n for _ in range(n)]
    cnt = 0
    for y in range(n):
        for x in range(n):
            if graph[y][x] > 0 and not visit[y][x]:
                cnt += 1
                dfs(x, y)
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
