import sys
from typing import List


def solution(nums: List[int]) -> int:
    answer = 1

    for num in sorted(nums):
        if num > answer:
            return answer

        answer += num

    return answer


N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

print(solution(nums))
