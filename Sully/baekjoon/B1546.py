def solution(nums):
    new_nums = []
    M = max(nums)

    for num in nums:
        new_nums.append(num / M * 100)

    return sum(new_nums) / len(new_nums)


# 파이썬은 N 구할 필요가 없지만..
N = int(input())
nums = list(map(int, input().split()))

print(solution(nums))
