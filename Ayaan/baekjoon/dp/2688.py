T = int(input())
for _ in range(T):
    n = int(input())
    dp = [[1] * 10 for _ in range(n + 1)]
    for i in range(2, n + 1):
        for j in range(10):
            # dp[i][j] = 이전 자리수 i의 j~9까지의 합
            dp[i][j] = sum(dp[i - 1][j:])
    print(sum(dp[n]))
