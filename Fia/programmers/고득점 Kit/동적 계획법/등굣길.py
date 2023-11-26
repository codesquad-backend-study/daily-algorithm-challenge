def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    puddles = set([(n, m) for m, n in puddles])

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1: continue
            if (i, j) in puddles: continue

            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[n][m] % 1_000_000_007
