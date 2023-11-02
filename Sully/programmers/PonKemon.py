def solution(nums):
    N = len(nums)
    half = N // 2

    nums_dict = {num: 0 for num in nums}

    if half <= len(nums_dict):
        return half

    # if half > len(nums_dict)
    return len(nums_dict)


print(solution([3, 1, 2, 3]))  # 2, {3, 1, 2}
print(solution([3, 3, 3, 2, 2, 4]))  # 3, {3, 2, 4}
print(solution([3, 3, 3, 2, 2, 2]))  # 3, {3, 2}
