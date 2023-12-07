import collections


def solution(maps):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    dist = [[-1] * len(maps[0]) for _ in range(len(maps))]

    queue = collections.deque()
    queue.append((0, 0))
    dist[0][0] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if 0 <= nx < len(maps[0]) and 0 <= ny < len(maps):
                if maps[ny][nx] == 1 and dist[ny][nx] == -1:
                    dist[ny][nx] = dist[y][x] + 1
                    queue.append((nx, ny))

    return dist[-1][-1]
