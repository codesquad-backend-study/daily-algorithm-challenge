n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]

d = [[0] * n for _ in range(n)]
d[0][0] = 1

for y in range(n):
    for x in range(n):
        if board[y][x] != 0 and d[y][x] != 0:
            if x + board[y][x] < n:
                d[y][x + board[y][x]] += d[y][x]

            if y + board[y][x] < n:
                d[y + board[y][x]][x] += d[y][x]

print(d[-1][-1])
