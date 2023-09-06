import sys
from typing import List


def solution(nums: List[int]) -> int:
    plus, minus, one = [], [], []

    for num in nums:
        if num > 1:
            plus.append(num)
            continue

        # 당연히 음수에 0이 포함돼야지 더 커짐
        if num <= 0:
            minus.append(num)
            continue

        # 양수, 음수 모두 더하는 게 더 커짐
        # if num == 1:
        one.append(num)

    plus.sort(reverse=True)
    minus.sort()

    answer = sum(one)

    # 양수, 음수 각각 계산
    for i in range(0, len(plus), 2):
        if i == len(plus) - 1:
            answer += plus[i]
            break

        answer += plus[i] * plus[i + 1]

    for i in range(0, len(minus), 2):
        if i == len(minus) - 1:
            answer += minus[i]
            break

        answer += minus[i] * minus[i + 1]

    return answer


N = int(sys.stdin.readline().rstrip())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline().rstrip()))

print(solution(nums))
