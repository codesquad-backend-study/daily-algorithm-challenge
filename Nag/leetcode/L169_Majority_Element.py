class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        majority = len(nums) // 2

        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
            if count[num] > majority:
                return num
