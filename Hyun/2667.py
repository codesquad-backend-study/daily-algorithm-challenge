def dfs(x, y):
    graph[y][x] = number

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if graph[ny][nx] == "1":
                dfs(nx, ny)


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

number = 0

n = int(input())
graph = [list(input()) for _ in range(n)]

for y in range(n):
    for x in range(n):
        if graph[y][x] == "1":
            number += 1
            dfs(x, y)

ans = []

for num in range(1, number+1):
    house_cnt = 0
    for y in range(n):
        for x in range(n):
            if graph[y][x] == num:
                house_cnt += 1

    ans.append(house_cnt)

ans.sort()

print(number)
print(*ans, sep="\n")
