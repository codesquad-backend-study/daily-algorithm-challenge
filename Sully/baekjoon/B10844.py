import sys


def solution(N: int) -> int:
    # dp[자리 수][자리 중 맨 뒤에 있는 숫자]
    dp = [[0] * 10 for _ in range(N + 1)]

    for i in range(1, 10):
        dp[1][i] = 1

    for i in range(2, N + 1):
        for j in range(10):
            # 0일 때는 당연히 1밖에 올 수 없는 거고
            if j == 0:
                dp[i][j] = dp[i - 1][1]
                continue

            # 9일 때도 8밖에 올 수 없음 (0과 똑같은 이유, 끝자리니까)
            if j == 9:
                dp[i][j] = dp[i - 1][8]
                continue

            # 1 <= j <= 8: 전의 자리 수에서 -1과 +1일 때를 더해주면 됨 (이때가 그 경우의 수)
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

    return sum(dp[N]) % 1000000000


N = int(sys.stdin.readline().rstrip())
print(solution(N))
