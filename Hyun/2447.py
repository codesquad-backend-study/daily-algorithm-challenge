n = int(input())

board = [[False] * n for _ in range(n)]


def fill(x, y, size):
    if size == 0:
        board[y][x] = True
        return

    for i in range(9):
        if i == 4:
            continue

        fill(x + size * (i % 3), y + size * (i // 3), size // 3)


def print_board(n):
    for y in range(n):
        for x in range(n):
            if board[y][x]:
                print('*', end="")
            else:
                print(' ', end="")
        print()


fill(0, 0, n // 3)
print_board(n)
