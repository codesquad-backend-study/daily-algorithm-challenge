import sys


def solution(N: int, r: int, c: int) -> None:
    answer = 0

    def quad_tree(n: float, x: float, y: float) -> None:
        nonlocal answer

        if r == x and c == y:
            print(int(answer))
            exit(0)

        if not (x <= r < x + n and y <= c < y + n):
            answer += n * n
            return

        mid = n / 2
        quad_tree(mid, x, y)
        quad_tree(mid, x, y + mid)
        quad_tree(mid, x + mid, y)
        quad_tree(mid, x + mid, y + mid)

    quad_tree(2 ** N, 0, 0)


N, r, c = map(int, sys.stdin.readline().rstrip().split())
solution(N, r, c)
