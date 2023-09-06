import sys
from typing import List


def solution(nums_list: List[List[int]]) -> List[int]:
    # 각각 처리한 행까지의 최솟값, 최댓값을 저장하는 리스트
    min_list, max_list = [0, 0, 0], [0, 0, 0]

    for nums in nums_list:
        min_list = [nums[0] + min(min_list[:2]),
                    nums[1] + min(min_list),
                    nums[2] + min(min_list[1:])]

        max_list = [nums[0] + max(max_list[:2]),
                    nums[1] + max(max_list),
                    nums[2] + max(max_list[1:])]

    return [max(max_list), min(min_list)]


N = int(sys.stdin.readline().rstrip())
nums_list: List[List[int]] = []
for _ in range(N):
    nums_list.append(list(map(int, sys.stdin.readline().rstrip().split())))

print(*solution(nums_list))
