from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        i = 0
        while True:
            if i == len(nums)-1:
                return nums[i]
            if nums[i] == nums[i+1]:
                i = i+2
                continue
            else:
                return nums[i]
        

solution = Solution()
num = solution.singleNumber([1,2,2,1,3])
print(num)