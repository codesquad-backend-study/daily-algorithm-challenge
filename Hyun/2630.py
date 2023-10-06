def divide(sx, sy, n):
    offset = n // 2

    start = board[sx][sy]
    white, blue = 0, 0

    for y in range(sx, sx + n):
        for x in range(sy, sy + n):
            if start != board[y][x]:
                result = divide(sx, sy, n // 2)
                white += result[0]
                blue += result[1]

                result = divide(sx + offset, sy, n // 2)
                white += result[0]
                blue += result[1]

                result = divide(sx, sy + offset, n // 2)
                white += result[0]
                blue += result[1]

                result = divide(sx + offset, sy + offset, n // 2)
                white += result[0]
                blue += result[1]

                return white, blue

    if start == 0:
        return white + 1, blue
    else:
        return white, blue + 1


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

white, blue = divide(0, 0, n)
print(white)
print(blue)
