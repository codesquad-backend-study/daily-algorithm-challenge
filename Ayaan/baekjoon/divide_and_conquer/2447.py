N = int(input())
star = [[0] * N for _ in range(N)]


def print_star(n):
    if n == 3:
        star[0][:3] = [1, 1, 1]
        star[1][:3] = [1, 0, 1]
        star[2][:3] = [1, 1, 1]
        return

    a = n // 3
    print_star(a)

    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                star[a * i + k][a * j: a * (j + 1)] = star[k][:a]


print_star(N)
for i in range(N):
    for j in range(N):
        if star[i][j] == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
