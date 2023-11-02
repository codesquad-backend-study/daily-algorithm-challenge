import sys

N = int(input())
nums = list(map(int, input().split()))
nums.sort(key=lambda x: abs(x), reverse=True)

min_mix = sys.maxsize
a = b = 0
for i in range(len(nums) - 1):
    if min_mix > abs(nums[i] + nums[i + 1]):
        min_mix = abs(nums[i] + nums[i + 1])
        a = nums[i]
        b = nums[i + 1]
print(min(a, b), end=" ")
print(max(a, b))
