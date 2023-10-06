def go(N, y, x):
    if N == 0:
        return 0
    return 2 * (y % 2) + (x % 2) + 4 * go(N - 1, y // 2, x // 2)


n, y, x = map(int, input().split())

print(go(n, y, x))
