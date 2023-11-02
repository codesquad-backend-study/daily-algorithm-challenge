def masking(sx, sy):                                    # 색종이 그리기
    for y in range(sy - 9, sy + 1):
        for x in range(sx, sx + 10):
            drawing_paper[y][x] = True


def calculate():                                        # 색종이 부분의 넓이 계산
    width = 0
    for y in range(100):
        for x in range(100):
            if drawing_paper[y][x]:
                width += 1
    return width


drawing_paper = [[False] * 100 for _ in range(100)]     # 흰 도화지

t = int(input())

for _ in range(t):
    sx, sy = map(int, input().split())
    masking(sx, sy)

print(calculate())