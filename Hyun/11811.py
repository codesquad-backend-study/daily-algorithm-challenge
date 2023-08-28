def count(num, x, y):
    one_cnt = bin(num).count('1')

    if series[x][1] < one_cnt:
        series[x] = (num, one_cnt)

    if series[y][1] < one_cnt:
        series[y] = (num, one_cnt)


n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

series = [(0, 0)] * n

for y in range(n):
    for x in range(y + 1, n):
        count(matrix[y][x], x, y)

for num, _ in series:
    print(num, end=' ')
