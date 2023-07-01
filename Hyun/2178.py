import collections

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

h, w = map(int, input().split())

graph = [list(input()) for _ in range(h)]
dist = [[-1] * w for _ in range(h)]

queue = collections.deque([(0, 0, 1)])
dist[0][0] = 1

while queue:
    x, y, distance = queue.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < w and 0 <= ny < h:
            if dist[ny][nx] == -1 and graph[ny][nx] == '1':
                queue.append((nx, ny, distance + 1))
                dist[ny][nx] = distance + 1

print(dist[h-1][w-1])
