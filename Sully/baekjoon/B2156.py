import sys
from typing import List


def solution(n: int, amounts: List[int]) -> int:
    amounts.insert(0, 0)

    dp = [0] * (n + 1)
    # 즉, 세번째부터라는 뜻
    dp[1] = amounts[1]

    if n >= 2:
        dp[2] = amounts[1] + amounts[2]

    for i in range(3, n + 1):
        dp[i] = max(
            # i번째 와인을 마시지 않고, 그 직전 와인까지만 마시는 경우
            dp[i - 1],
            # i번째 와인만 마시는 경우
            dp[i - 2] + amounts[i],
            # i - 1번째 와인과 i번째 와인을 함께 마시는 경우
            dp[i - 3] + amounts[i - 1] + amounts[i]
        )

    return dp[n]


n = int(sys.stdin.readline().rstrip())
amounts = []
for _ in range(n):
    amounts.append(int(sys.stdin.readline().rstrip()))

print(solution(n, amounts))
