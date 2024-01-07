import collections


def solution(arrows):
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    cx = 0
    cy = 0

    points = set([(0, 0)])
    edges = set()
    count = 0

    for arrow in arrows:
        for _ in range(2):  # 대각선을 검증하기 위해 그래프를 2배로 늘려서 사용한다
            nx = cx + dx[arrow]
            ny = cy + dy[arrow]

            if (nx, ny) in points:
                if (cx, cy, nx, ny) not in edges and (nx, ny, cx, cy) not in edges:
                    count += 1

                edges.add((cx, cy, nx, ny))
                cx = nx
                cy = ny
                continue

            points.add((nx, ny))
            edges.add((cx, cy, nx, ny))

            cx = nx
            cy = ny

    return count
