import collections


def solution(nums):
    mid = len(nums) // 2
    dict = collections.defaultdict(int)

    for num in nums:
        dict[num] += 1

    if len(dict) < mid:
        return len(dict)

    return mid


print(solution([3, 3, 3, 2, 2, 4]))
