import collections


def solution(nums):
    remainders = collections.defaultdict(int)

    for num in nums:
        remainders[num % 42] += 1

    return len(remainders)


nums = []
for _ in range(10):
    nums.append(int(input()))

print(solution(nums))
