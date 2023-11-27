from collections import deque


def solution(maps):
    queue = deque([(0, 0, 0)])
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    while queue:
        row, column, distance = queue.popleft()

        if visited[row][column] == 0:
            visited[row][column] = distance + 1
        else:
            continue

        for i in range(4):
            if 0 <= row + dx[i] < len(maps) and 0 <= column + dy[i] < len(maps[0]):
                if maps[row + dx[i]][column + dy[i]] != 0 and visited[row + dx[i]][column + dy[i]] == 0:
                    queue.append((row + dx[i], column + dy[i], distance + 1))

    return visited[-1][-1] if visited[-1][-1] != 0 else -1
