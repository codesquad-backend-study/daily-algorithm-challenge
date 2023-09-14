n, k = map(int, input().split())
nums = [int(input()) for _ in range(n)]
# dp[i] = i원을 만들 수 있는 경우의 수
dp = [0] * (k + 1)
dp[0] = 1

for num in nums:
    for value in range(num, k + 1):
        # value원으로 만들 수 있는 경우의 수
        # 이전의 value원을 만든 경우의 수 + (value원을 하나 뺀 나머지)원을 만들 수 있는 경우의 수
        dp[value] = dp[value] + dp[value - num]

print(dp[k])
