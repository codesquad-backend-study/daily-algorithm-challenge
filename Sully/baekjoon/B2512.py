import sys
from typing import List


def solution(M: int, nums: List[int]) -> int:
    # lt: 최소 num
    # rt: 최대 num
    lt, rt = 0, max(nums)

    while lt <= rt:
        mid = (lt + rt) // 2
        current = 0

        for num in nums:
            # 예산(num)이 상한액(mid)보다 클 경우 -> 상한액을 지급해나가면 됨
            if num >= mid:
                current += mid
                continue

            # 예산(num)이 상한액(mid)보다 작을 경우 -> 예산 지급
            current += num

        # 지급 예정인 금액(current)가 M보다 작거나 같을 경우 -> 상한액을 높여줘야 함
        if current <= M:
            lt = mid + 1
            continue

        rt = mid - 1

    return rt


N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())

print(solution(M, nums))
