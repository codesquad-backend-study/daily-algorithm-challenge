from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    road = [[False] * 101 for _ in range(101)]

    # 선분 4개 그리기
    for left_bottom_x, left_bottom_y, right_top_x, right_top_y in rectangle:

        min_row = left_bottom_y * 2
        max_row = right_top_y * 2
        min_col = left_bottom_x * 2
        max_col = right_top_x * 2

        for i in range(min_row, max_row + 1):
            road[i][min_col] = True
            road[i][max_col] = True

        for i in range(min_col, max_col + 1):
            road[min_row][i] = True
            road[max_row][i] = True

    # 사각형 내부의 선분 모두 지우기
    for left_bottom_x, left_bottom_y, right_top_x, right_top_y in rectangle:

        min_row = left_bottom_y * 2
        max_row = right_top_y * 2
        min_col = left_bottom_x * 2
        max_col = right_top_x * 2

        for i in range(min_row + 1, max_row):
            for j in range(min_col + 1, max_col):
                road[i][j] = False

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque([(characterY * 2, characterX * 2, 0)])

    while queue:
        row, col, distance = queue.popleft()
        road[row][col] = distance

        for i in range(4):
            if 0 < row + dx[i] <= 100 and 0 < col + dy[i] <= 100 and road[row + dx[i]][col + dy[i]] == True:
                queue.append((row + dx[i], col + dy[i], distance + 1))

    return road[itemY * 2][itemX * 2] // 2
