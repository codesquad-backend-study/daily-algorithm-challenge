N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

minus = 0
zero = 0
plus = 0


def solution(x, y, n):
    global minus
    global zero
    global plus

    a = n // 3
    temp = data[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if temp != data[i][j]:
                solution(x, y, a)
                solution(x, y + a, a)
                solution(x, y + (2 * a), a)
                solution(x + a, y, a)
                solution(x + a, y + a, a)
                solution(x + a, y + (2 * a), a)
                solution(x + (2 * a), y, a)
                solution(x + (2 * a), y + a, a)
                solution(x + (2 * a), y + (2 * a), a)
                return

    if temp == -1:
        minus += 1
    elif temp == 0:
        zero += 1
    else:
        plus += 1


solution(0, 0, N)
print(minus)
print(zero)
print(plus)
