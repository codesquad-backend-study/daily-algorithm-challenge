# 재귀보다 dp가 훨씬 빠르니 재귀 사용 x

def fibo(n):
    # 0이나 1일 경우 생각 x
    if n == 0:
        return 0
    if n == 1:
        return 1

    # 빈 dp 배열의 길이가 n + 1인 이유: n은0부터 시작하니까
    dp = [0] * (n + 1)

    # 초기값 설정
    dp[0], dp[1] = 0, 1

    # 초기값은 위에서 설정해 주었으니 점화식을 위해 2부터
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


print(fibo(int(input())))
