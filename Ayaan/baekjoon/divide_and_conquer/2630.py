N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
blue = 0
white = 0


def slice(x, y, n):
    global blue
    global white

    mid = n // 2
    temp = data[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 첫번째 색과 다른 색이 나오면 4등분 해서 재귀로 다시 실행한다.
            if data[i][j] != temp:
                slice(x, y, mid)
                slice(x, y + mid, mid)
                slice(x + mid, y, mid)
                slice(x + mid, y + mid, mid)
                return

    if temp:
        blue += 1
    else:
        white += 1


slice(0, 0, N)
print(white)
print(blue)
