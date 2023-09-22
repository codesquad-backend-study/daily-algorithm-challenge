counter = {-1: 0, 0: 0, 1: 0}


def divide(sx, sy, n):
    div = n // 3
    start = board[sy][sx]

    for y in range(sy, sy + n):
        for x in range(sx, sx + n):
            if start != board[y][x]:
                divide(sx, sy, div)
                divide(sx + div, sy, div)
                divide(sx + 2 * div, sy, div)

                divide(sx, sy + div, div)
                divide(sx + div, sy + div, div)
                divide(sx + 2 * div, sy + div, div)

                divide(sx, sy + 2 * div, div)
                divide(sx + div, sy + 2 * div, div)
                divide(sx + 2 * div, sy + 2 * div, div)

                return

    counter[start] += 1


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

divide(0, 0, n)

for _, ans in counter.items():
    print(ans)
