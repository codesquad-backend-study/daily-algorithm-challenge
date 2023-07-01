import collections

dx = [1, 2, 2, 1, -1, -2, -2, -1]
dy = [2, 1, -1, -2, -2, -1, 1, 2]

t = int(input())

for _ in range(t):
    n = int(input())
    graph = [[-1] * n for _ in range(n)]

    current_x, current_y = map(int, input().split())
    destination_x, destination_y = map(int, input().split())

    queue = collections.deque([(current_x, current_y, 0)])
    graph[current_y][current_x] = 0

    while queue:
        x, y, cnt = queue.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if graph[ny][nx] == -1:
                    queue.append((nx, ny, cnt + 1))
                    graph[ny][nx] = cnt + 1

    print(graph[destination_y][destination_x])
