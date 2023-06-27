# 미로 탐색
import collections

row, column = map(int, input().split())
board = [list(input()) for _ in range(row)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

queue = collections.deque([(0, 0, 1)])
visited = [[False] * column for _ in range(row)]
visited[0][0] = True

while queue:
    current = queue.popleft()

    if current[0] == row - 1 and current[1] == column - 1:
        print(current[2])
        break

    for i in range(4):
        next_row = dy[i] + current[0]
        next_column = dx[i] + current[1]
        if 0 <= next_row < row and 0 <= next_column < column:
            if not visited[next_row][next_column] and board[next_row][next_column] == '1':
                visited[next_row][next_column] = True
                queue.append((next_row, next_column, current[2] + 1))



