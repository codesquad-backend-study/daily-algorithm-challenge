N = int(input())
wines = [0] * (N + 2)
for i in range(N):
    wines[i] = int(input())

dp = [0] * (N + 2)
dp[0] = wines[0]
dp[1] = wines[0] + wines[1]
dp[2] = max(dp[1], wines[0] + wines[2], wines[1] + wines[2])

for i in range(3, len(wines)):
    dp[i] = max(dp[i - 2] + wines[i], dp[i - 3] + wines[i - 1] + wines[i], dp[i - 1])

print(max(dp))
