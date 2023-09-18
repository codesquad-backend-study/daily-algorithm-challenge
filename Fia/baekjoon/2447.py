# 별 찍기 - 10

N = int(input())


def draw_star(size):
    if size == 3:
        return ["***", "* *", "***"]

    group = draw_star(size // 3)
    stars = []

    for i in group:
        stars.append(i * 3)

    for i in group:
        stars.append(i + " " * (size // 3) + i)

    for i in group:
        stars.append(i * 3)

    return stars


print('\n'.join(draw_star(N)))
