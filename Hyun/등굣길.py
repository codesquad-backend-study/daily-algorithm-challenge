def solution(m, n, puddles):
    puddle_set = set([tuple(each) for each in puddles])
    global ans
    ans = 0

    def go(x, y):
        if (x, y) in puddle_set:
            return

        if x == m and y == n:
            global ans
            ans += 1
            return

        if x + 1 <= m:
            go(x + 1, y)

        if y + 1 <= n:
            go(x, y + 1)

    go(1, 1)

    return ans % 1_000_000_007


# 시간초과 코드
# ====================================================


def solution(m, n, puddles):
    d = [[0] * m for _ in range(n)]
    puddle_set = set([tuple(each) for each in puddles])

    d[0][0] = 1

    for y in range(n):
        for x in range(m):
            if y == 0 and x == 0:
                continue

            if (x + 1, y + 1) in puddle_set:
                continue

            if x > 0:
                d[y][x] += d[y][x - 1]

            if y > 0:
                d[y][x] += d[y - 1][x]

    return d[-1][-1] % 1_000_000_007

# DP로 풀이하면 시간내에 풀린다.
