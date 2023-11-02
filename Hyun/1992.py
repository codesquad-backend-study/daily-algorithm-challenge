def divide(sx, sy, n):
    start = board[sy][sx]
    offset = n // 2

    stat = str(start)

    for y in range(sy, sy + n):
        for x in range(sx, sx + n):
            if start != board[y][x]:
                lu = divide(sx, sy, offset)
                ru = divide(sx + offset, sy, offset)
                ld = divide(sx, sy + offset, offset)
                rd = divide(sx + offset, sy + offset, offset)

                return "(" + lu + ru + ld + rd + ")"

    return stat


n = int(input())
board = [list(map(int, list(input()))) for _ in range(n)]

print(divide(0, 0, n))
