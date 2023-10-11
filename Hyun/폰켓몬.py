import collections


def solution(nums):
    dict = collections.defaultdict(int)

    for num in nums:
        dict[num] += 1

    if len(nums) // 2 <= len(dict):
        return len(nums) // 2
    else:
        return len(dict)
