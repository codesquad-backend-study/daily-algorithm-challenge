import sys
from typing import List


def solution(cases: List[int], k: int) -> int:
    cases.sort()

    dp = [0] * (k + 1)
    # dp[k - k] = dp[0] -> 합이 k가 될 때 = k원 동전 하나는 쓰는 경우
    dp[0] = 1
    for case in cases:
        # i - case가 음수가 되지 않도록 case부터 시작
        for i in range(case, k + 1):
            dp[i] += dp[i - case]

    return dp[k]


n, k = map(int, sys.stdin.readline().rstrip().split())
cases: List[int] = []
for _ in range(n):
    cases.append(int(sys.stdin.readline().rstrip()))

print(solution(cases, k))
