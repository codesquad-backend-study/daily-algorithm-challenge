from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def find_set(board, flag):
    length = len(board)
    sets = []
    visited = [[False] * length for _ in range(length)]

    for i in range(length):
        for j in range(length):
            if not visited[i][j] and board[i][j] == flag:
                queue = deque([(i, j)])
                visited[i][j] = True
                spaces = [(i, j)]

                while queue:
                    x, y = queue.popleft()

                    for d in range(4):
                        nx = x + dx[d]
                        ny = y + dy[d]

                        if 0 <= nx < length and 0 <= ny < length:
                            if board[nx][ny] == flag and not visited[nx][ny]:
                                queue.append((nx, ny))
                                visited[nx][ny] = True
                                spaces.append((nx, ny))

                sets.append(spaces)

    return sets


def make_table(sets):
    x, y = zip(*sets)
    row_min = min(x)
    col_min = min(y)

    row_len = max(x) - row_min + 1
    col_len = max(y) - col_min + 1
    table = [[0] * col_len for _ in range(row_len)]

    for r, c in sets:
        r = r - row_min
        c = c - col_min
        table[r][c] = 1

    return table


def rotate(puzzle):
    rotated = [[0] * len(puzzle) for _ in range(len(puzzle[0]))]
    count = 0

    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 1:
                count += 1
            rotated[j][len(puzzle) - i - 1] = puzzle[i][j]

    return rotated, count


def solution(game_board, table):
    answer = 0
    empty_blocks = find_set(game_board, 0)
    puzzles = find_set(table, 1)

    for block in empty_blocks:
        filled = False
        block = make_table(block)

        for origin_puzzle in puzzles:
            if filled:
                break

            puzzle = make_table(origin_puzzle)

            for i in range(4):
                puzzle, count = rotate(puzzle)

                if block == puzzle:
                    answer += count
                    puzzles.remove(origin_puzzle)
                    filled = True
                    break

    return answer


print(solution([[1, 1, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 1, 1, 0, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 0, 0, 1, 0], [0, 1, 1, 1, 0, 0]], [[1, 0, 0, 1, 1, 0], [1, 0, 1, 0, 1, 0], [0, 1, 1, 0, 1, 1], [0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 1, 0], [0, 1, 0, 0, 0, 0]]))
